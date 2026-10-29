import csv
import math
import re
import unicodedata
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = ROOT / "loops_plan" / "9_loop"
LEVELS = ("A1", "A2", "B1", "B2")
SUFFIX = re.compile(
    r"(?:\b(?:n|v|adj|adv|prep|conj|det|pron|exclam)\."
    r"(?:\s*[,/]\s*(?:n|v|adj|adv|prep|conj|det|pron|exclam)\.)*"
    r"|\b(?:number|auxiliary verb|modal verb|indefinite article|"
    r"definite article|infinitive marker|ordinal number))\s*$"
)


def norm(value):
    return " ".join(unicodedata.normalize("NFKC", value).split()).casefold()


def clean(value):
    return " ".join(value.replace("\u00a0", " ").split())


def source_head(raw):
    match = re.search(
        r"\s+(?=(?:n\.|v\.|adj\.|adv\.|prep\.|conj\.|det\.|pron\.|exclam\.|"
        r"number\b|auxiliary verb\b|modal verb\b|indefinite article\b|"
        r"definite article\b|infinitive marker\b|ordinal number\b))",
        raw,
    )
    prefix = raw[:match.start()].strip() if match else raw
    return re.sub(r"\s*\([^)]*\)$", "", prefix).strip()


def old_head(raw):
    raw = clean(raw)
    match = re.search(
        r"\s+(?:n\.|v\.|adj\.|adv\.|prep\.|conj\.|det\.|pron\.|exclam\.).*$",
        raw,
    )
    return raw[:match.start()].strip() if match else raw


def esc(value):
    return str(value).replace("|", r"\|").replace("\n", " ").replace("\r", " ")


def main():
    base_plan = (BASE / "1_plan_estudio_por_sesiones_de_repeticion.md").read_text(
        encoding="utf-8"
    )
    with (BASE / "2_catalogo_trazabilidad_fuentes.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        old_rows = list(csv.DictReader(stream, delimiter=";"))
    fields = list(old_rows[0])

    records = []
    state = None
    pdf = pymupdf.open(ROOT / "resources" / "Oxford 3000_by CEFR level.pdf")
    for page_num, page in enumerate(pdf, 1):
        lines = page.get_text().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line in LEVELS:
                state = line
                i += 1
                continue
            if (
                not state
                or not line
                or line.startswith("The Oxford 3000")
                or re.fullmatch(r"\d+ / 12", line)
                or "Oxford University Press" in line
            ):
                i += 1
                continue
            raw, end = line, i + 1
            while not SUFFIX.search(raw) and end < len(lines):
                nxt = lines[end].strip()
                if not nxt or nxt in LEVELS or nxt.startswith("The Oxford 3000"):
                    break
                raw += " " + nxt
                end += 1
            if SUFFIX.search(raw):
                raw = clean(raw)
                records.append(
                    {
                        "level": state,
                        "page": page_num,
                        "line_start": i + 1,
                        "line_end": end,
                        "raw": raw,
                        "head": source_head(raw),
                    }
                )
            i = end

    counts = {lev: sum(r["level"] == lev for r in records) for lev in LEVELS}
    assert counts == {"A1": 900, "A2": 871, "B1": 809, "B2": 726}, counts
    assert len(records) == 3306
    assert len({norm(r["raw"]) for r in records}) == 3306

    old_by_head = {}
    for row in old_rows:
        old_by_head.setdefault(norm(old_head(row["entrada_fuente_raw_pypdf"])), []).append(row)
    related = {
        (r["level"], r["page"], r["line_start"]): old_by_head[norm(r["head"])]
        for r in records
        if old_by_head.get(norm(r["head"]))
    }
    phone_phrase = [
        r
        for r in old_rows
        if r["pdf_fuente"] == "Oxford Phrase List.pdf"
        and norm(r["entrada_normalizada"]) == "phone number"
    ]
    assert len(phone_phrase) == 1
    phone = [r for r in records if norm(r["head"]) == "phone"]
    assert len(phone) == 1

    max_session = {}
    for row in old_rows:
        match = re.fullmatch(r"(A1|A2|B1|B2|C1|C2)-S(\d+)", row["sesion_plan"])
        if match:
            lev = match.group(1)
            max_session[lev] = max(max_session.get(lev, 0), int(match.group(2)))
    max_session["C2"] = 12  # C2 has integration sessions, not lexical catalog rows.
    assert max_session == {"A1": 26, "A2": 19, "B1": 20, "B2": 71, "C1": 117, "C2": 12}

    grammar_bank = {lev: [] for lev in LEVELS}
    for line in base_plan.splitlines():
        for lev in LEVELS:
            if f"**{lev}-S" not in line:
                continue
            columns = line.split("|")
            if len(columns) < 6:
                continue
            cell = columns[4]
            match = re.search(
                r"(?:Introducir|Recuperar/aplicar)\s+(G\d{2}):\s*(.*?)"
                r"(?:\.\s*(?:Repasar|Recuperar/aplicar|Introducir)\s+G\d{2}:|\s*\|?$)",
                cell,
            )
            if match:
                item = (match.group(1), match.group(2).strip().rstrip("."))
                if item not in grammar_bank[lev]:
                    grammar_bank[lev].append(item)
    for lev in LEVELS:
        if not grammar_bank[lev]:
            grammar_bank[lev] = [("G01", "recuperación integrada de estructuras ya introducidas")]

    def sid(lev, local):
        return f"{lev}-S{max_session[lev] + local:03d}"

    cohorts = {}
    for lev in LEVELS:
        items = [r for r in records if r["level"] == lev]
        cohort_count = math.ceil(len(items) / 12)
        cohorts[lev] = {}
        for j in range(1, cohort_count + 1):
            cohort = items[(j - 1) * 12 : j * 12]
            cohorts[lev][j] = cohort
            for k, record in enumerate(cohort, 1):
                record["session"] = sid(lev, j)
                record["unit_id"] = f"O3K-{lev}-{j:03d}-U{k:02d}"
                preceding = sum(counts[x] for x in LEVELS[: LEVELS.index(lev)])
                record["canonical"] = f"O3K-{preceding + (j - 1) * 12 + k:05d}"
                record["review_sessions"] = {gap: sid(lev, j + gap) for gap in (1, 3, 6)}
        expected = {"A1": 81, "A2": 79, "B1": 74, "B2": 67}[lev]
        assert cohort_count + 6 == expected

    sessions = []
    for lev in LEVELS:
        cohort_count = math.ceil(counts[lev] / 12)
        for j in range(1, cohort_count + 7):
            new_units = cohorts[lev].get(j, [])
            review_cohorts = [
                (gap, j - gap, cohorts[lev][j - gap])
                for gap in (1, 3, 6)
                if j - gap in cohorts[lev]
            ]
            review_count = sum(len(cohort) for _, _, cohort in review_cohorts)
            new_count = len(new_units)
            p_new, p_review, p_grammar = new_count * 5, review_count, 30
            p_integration = 150 - p_new - p_review - p_grammar
            assert p_integration >= (24 if new_count else 84)
            assert p_new + p_review + p_grammar + p_integration == 150
            gcode, gfocus = grammar_bank[lev][(j - 1) % len(grammar_bank[lev])]
            grammar = (
                f"Recuperar {gcode}: {gfocus}; practicarlo en 30 pares orales breves, "
                "sin introducir otro foco gramatical."
            )
            if new_count:
                objective = {
                    "A1": "Usar las unidades léxicas impresas en microintercambios inmediatos (descripción, petición, pregunta y respuesta), respetando categoría y sentido; producir cinco pares naturales por unidad sin forzar un tema único.",
                    "A2": "Usar las unidades léxicas impresas en microescenas de rutinas, servicios, desplazamientos y experiencias; variar pregunta, respuesta y contraste, respetando categoría y sentido.",
                    "B1": "Integrar las unidades léxicas impresas al narrar experiencias, explicar decisiones y expresar opiniones en contextos cotidianos variados, respetando categoría y sentido.",
                    "B2": "Aplicar las unidades léxicas impresas al explicar procesos, matizar afirmaciones y resolver situaciones profesionales/cotidianas, respetando categoría y sentido.",
                }[lev]
                focus = "; ".join(f"{r['unit_id']}: {esc(r['raw'])}" for r in new_units)
            else:
                objective = "Recuperar en contextos nuevos las cohortes léxicas asignadas a +1/+3/+6; reformular enunciados y mantener la acepción y el nivel impresos, sin introducir léxico nuevo."
                focus = "Sin unidades nuevas. Integración acumulativa del nivel y recuperación contextual; ver términos y fechas de repaso en las unidades indicadas en el campo de repaso."

            review_parts = []
            for gap, source_j, cohort in review_cohorts:
                terms = ", ".join(f"{r['unit_id']} {esc(r['raw'])}" for r in cohort)
                review_parts.append(f"+{gap} {sid(lev, source_j)}: {terms}")
            review = "; ".join(review_parts) or (
                "Sin cohorte Oxford 3000 vencida en +1/+3/+6; integrar vocabulario previo del plan "
                "en el bloque acumulativo."
            )
            review += (
                f"; integración acumulativa: {p_integration} pares para recuperación de sesiones "
                "previas del nivel y contextos mixtos (sin nuevas asignaciones)."
            )
            sessions.append(
                {
                    "id": sid(lev, j),
                    "level": lev,
                    "local_index": j,
                    "kind": "Introducción léxica" if new_count else "Repaso espaciado/integración",
                    "objective": objective,
                    "focus": focus,
                    "grammar": grammar,
                    "review": review,
                    "new_count": new_count,
                    "review_count": review_count,
                    "pairs_new": p_new,
                    "pairs_review": p_review,
                    "pairs_grammar": p_grammar,
                    "pairs_integration": p_integration,
                    "total": 150,
                    "global_order": 266 + len(sessions),
                    "cohorts": "; ".join(
                        f"+{gap} {sid(lev, source_j)}"
                        for gap, source_j, _ in review_cohorts
                    )
                    or "—",
                }
            )

    new_catalog = []
    for r in records:
        refs = related.get((r["level"], r["page"], r["line_start"]), [])
        if norm(r["head"]) == "phone":
            refs = refs + phone_phrase
        source_refs = list(dict.fromkeys(x["codigo_unidad_intro"] or x["registro_fuente"] for x in refs))
        note = (
            "Texto y sentido conservados como aparecen en la página; normalización solo Unicode/"
            "espacios y minúsculas para búsqueda. No se colapsa por forma entre niveles ni categorías."
        )
        status = "unidad nueva; sin cobertura semántica exacta previa"
        if refs:
            status = "unidad nueva; exposición/solapamiento formal parcial, no cubierta como acepción independiente"
            note += " Referencia preexistente: " + ", ".join(
                f"{x['sesion_plan']} ({x['entrada_fuente_raw_pypdf']})" for x in refs
            ) + ". La categoría/sentido no es equivalente; se conserva como nueva unidad."
        row = {key: "" for key in fields}
        row.update(
            {
                "registro_fuente": f"O3K-{r['level']}-P{r['page']:02d}-L{r['line_start']:03d}",
                "pdf_fuente": "Oxford 3000_by CEFR level.pdf",
                "nivel_cefr_fuente": r["level"],
                "pagina_pdf": str(r["page"]),
                "linea_texto_extraido_inicio": str(r["line_start"]),
                "linea_texto_extraido_fin": str(r["line_end"]),
                "entrada_fuente_raw_pypdf": r["raw"],
                "entrada_normalizada": norm(r["raw"]),
                "id_unidad_canonica": r["canonical"],
                "sesion_plan": r["session"],
                "ubicacion_plan": f"1_plan_estudio_por_sesiones_de_repeticion.md#{r['session']} — Vocabulario Foco",
                "estado": status,
                "codigo_unidad_intro": r["unit_id"],
                "codigo_origen_si_duplicada": ", ".join(source_refs),
                "repaso_mas_1": r["review_sessions"][1],
                "repaso_mas_3": r["review_sessions"][3],
                "repaso_mas_6": r["review_sessions"][6],
                "categoria_visual_fuente": "Entrada léxica del Oxford 3000 (PDF)",
                "rol_cobertura": "Unidad nueva de nivel y acepción; fuente directa, con exposición formal relacionada si se indica.",
                "nota_normalizacion_pedagogica": note,
            }
        )
        new_catalog.append(row)

    # Quantitative overview and all session rows in level-separated tables.
    addon = [
        "## Iteración 10 — Integración trazable del Oxford 3000",
        "",
        "### Auditoría de cobertura y suficiencia de sesiones",
        "",
        "El PDF se cotejó directamente página por página. El título editorial dice Oxford 3000, pero la extracción de las entradas impresas produce **3306 registros léxicos con etiqueta CEFR** (A1–B2) y **2990 etiquetas de encabezado distintas** (una etiqueta, `a, an`, contiene dos formas). Las 316 apariciones adicionales son encabezados repetidos entre niveles/acepciones; se conservan con su propio nivel, texto fuente y página. No hay líneas exactas completas duplicadas en la extracción. El catálogo v10 contiene el texto extraído, su número de página y las líneas de extracción verificables.",
        "",
        "**Criterio de deduplicación:** se considera cubierto solo el mismo encabezado con categoría/acepción compatible, no una forma ortográfica que aparece con otra categoría ni la mera presencia de una palabra dentro de una expresión. Se localizaron 21 registros de Oxford 3000 con solapamiento formal de encabezado con Oxford 5000 (incluye dos acepciones de `rock`) y una exposición parcial de `phone` dentro de `phone number` en Phrase List. Ninguno coincide como unidad semántica independiente; por tanto **0 unidades se cuentan como cubiertas**, las 22 exposiciones se anotan y enlazan, y las 3306 entradas fuente se conservan como unidades nuevas que deben practicarse. No se declara equivalencia de sentido por coincidencia ortográfica.",
        "",
        "| Nivel fuente | Registros fuente | Cubiertos exactamente | Solapamientos parciales (enlazados) | Unidades nuevas asignadas | Sesiones de introducción nuevas | Sesiones adicionales de repaso | Total sesiones nuevas |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for lev in LEVELS:
        total = counts[lev]
        overlaps = sum(
            1
            for r in records
            if r["level"] == lev
            and (
                bool(related.get((r["level"], r["page"], r["line_start"])))
                or norm(r["head"]) == "phone"
            )
        )
        intros = math.ceil(total / 12)
        addon.append(f"| {lev} | {total} | 0 | {overlaps} | {total} | {intros} | 6 | {intros + 6} |")
    addon += [
        "| **Total A1–B2** | **3306** | **0** | **22** | **3306** | **277** | **24** | **301** |",
        "",
        "Los solapamientos parciales se incluyen dentro de las unidades nuevas (no son conteos aditivos): 21 coincidencias de encabezado con Oxford 5000 de categoría/sentido no equivalente y una aparición como componente de una expresión Phrase List. En A1 son 9 registros parciales (8 con Oxford 5000 + `phone`/`phone number`); A2, 9; B1, 3; B2, 1. Los términos, referencias a sesiones preexistentes y estados están fila por fila en `2_catalogo_trazabilidad_fuentes.csv`. Se citan **18 sesiones preexistentes distintas** para mostrar esas exposiciones; **0 se reutilizan como sesión de introducción** porque los sentidos/categorías no son duplicados. Las 265 sesiones de la iteración 9 se conservan sin alterar.",
        "",
        "**Cálculo verificable de capacidad.** Las sesiones preexistentes están diseñadas para 150 pares y no tienen capacidad libre que pueda presumirse. Para mantener carga oral acotada se usan como máximo 12 unidades nuevas por sesión: 5 pares de primera práctica por unidad (12×5=60), hasta 36 pares de repaso espaciado (tres cohortes de 12, un par por unidad y evento +1/+3/+6), 30 pares para gramática y mínimo 24 pares para integración; 60+36+30+24=150. Por nivel, se requieren `ceil(unidades nuevas/12)` sesiones de introducción: A1 `ceil(900/12)=75`; A2 `ceil(871/12)=73`; B1 `ceil(809/12)=68`; B2 `ceil(726/12)=61`; total **277**. La última cohorte de cada nivel requiere que existan las sesiones +1, +3 y +6, lo que justifica **seis sesiones posteriores por nivel** (24 adicionales; no son opcionales ni se cuentan como capacidad libre). Resultado mínimo: **301 sesiones nuevas** (277 de introducción +24 de repaso), no 277. El plan crece de 265 a **566 sesiones**; C1 y C2 no reciben vocabulario fuente nuevo porque el PDF no tiene esas secciones.",
        "",
        "**Programación de los repasos:** cada unidad nueva recibe cinco pares de primera práctica en su sesión y un par contextual en cada sesión identificada +1, +3 y +6; los identificadores exactos están en el catálogo. Los seis cierres de cada nivel permiten completar el +6 de la cohorte final. Cada sesión usa `5×nuevas + 1×eventos de repaso + 30 gramática + integración = 150`; si una cohorte es parcial o la sesión es solo repaso, se incrementa la integración, nunca se excede el máximo. Los pares de integración recuperan léxico de sesiones previas del nivel y contextos mixtos. Los 30 pares gramaticales recuperan estructuras ya introducidas, sin fingir léxico nuevo ni alterar los repasos previos del catálogo.",
        "",
        "**Orden global del suplemento:** para no desplazar ninguna de las 265 sesiones ni alterar sus destinos existentes de repetición espaciada, las 301 sesiones nuevas se añaden después del itinerario aprobado (órdenes globales 266–566). Dentro de ese suplemento se recorren bloques A1→A2→B1→B2; cada bloque conserva su orden y sus eventos +1/+3/+6. Las sesiones C2 preexistentes mantienen sus órdenes 254–265.",
        "",
        "### Sesiones de ampliación por nivel",
        "",
        "Las siguientes tablas son las sesiones de trabajo añadidas; la misma programación está disponible en `3_sesiones_oxford3000.csv`. El campo Vocabulario Foco enumera el texto fuente de cada unidad nueva; el campo Vocabulario en repaso enumera términos exactos de cada cohorte +1/+3/+6. La columna de pares permite verificar 150 por fila. En las sesiones de solo repaso no se agregan entradas léxicas.",
        "",
    ]
    for lev in LEVELS:
        addon += [
            f"#### {lev} — ampliación Oxford 3000",
            "",
            "| ID | Orden global | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso | Reparto de 150 pares |",
            "|---|---:|---|---|---|---|---|",
        ]
        for session in (x for x in sessions if x["level"] == lev):
            allocation = (
                f"{session['pairs_new']} nuevas + {session['pairs_review']} repaso espaciado + "
                f"{session['pairs_grammar']} gramática + {session['pairs_integration']} integración "
                f"= {session['total']}"
            )
            cells = [
                session["id"],
                session["global_order"],
                session["objective"],
                session["focus"],
                session["grammar"],
                session["review"],
                allocation,
            ]
            addon.append("| " + " | ".join(esc(value) for value in cells) + " |")
        addon.append("")
    addon += [
        "### Límites de evidencia no resueltos",
        "",
        "- La cifra editorial “Oxford 3000” no coincide con el número de registros de entrada con etiqueta CEFR extraídos del PDF. Este plan no elimina filas para forzar 3000: conserva los 3306 registros y las 2990 etiquetas de encabezado distintas (una etiqueta, `a, an`, contiene dos formas); los registros mantienen el texto impreso y la página para una revisión posterior si Oxford define otro criterio editorial de conteo.",
        "- La coincidencia de forma no permite inferir por sí sola acepción ni cobertura oral. Los 22 casos parciales se registran, enlazan a las sesiones existentes y se mantienen como nuevos objetivos cuando no hay identidad de categoría/acepción. No se pudo aplicar una eliminación adicional sin riesgo de perder sentidos.",
        "- No hay secciones C1/C2 del Oxford 3000 en este PDF; el vocabulario de esos niveles no se extrapola ni reasigna.",
    ]
    addon_text = "\n".join(addon) + "\n"

    plan = base_plan.replace(
        "# Plan de estudio por sesiones de repetición — Iteración 9 (A1–C2)",
        "# Plan de estudio por sesiones de repetición — Iteración 10 (A1–C2)",
    )
    plan = plan.replace(
        "## Alcance, marco y límites de la evidencia\n",
        "## Alcance, marco y límites de la evidencia\n\n"
        "**Actualización v10:** este documento conserva las 265 sesiones, las tablas y catálogos aprobados de la iteración 9 e incorpora el vocabulario Oxford 3000 cotejado directamente con el PDF. El análisis y las sesiones de ampliación v10 se presentan al final; las cifras de las secciones heredadas describen la línea base de la iteración 9, no el total actualizado.\n",
    )
    plan = plan.replace(
        "Marco cotejado directamente desde los dos PDFs del workspace:",
        "Marco preexistente cotejado directamente desde los dos PDFs del workspace:",
    )
    plan = plan.replace(
        "`resources/Oxford Phrase List.pdf`. Ninguno",
        "`resources/Oxford Phrase List.pdf`. La integración v10 incorpora además "
        "`resources/Oxford 3000_by CEFR level.pdf`, con cobertura y asignación descritas "
        "en el addendum. Ninguno",
    )
    plan = plan.replace(
        "### Recuento reconciliado del Oxford Phrase List y cobertura de fuentes",
        "### Línea base heredada (iteración 9): recuento reconciliado del Oxford Phrase List y cobertura de fuentes",
    )
    plan = plan.replace(
        "### Aplicación de observaciones de la iteración 4",
        "### Aplicación histórica de observaciones de la iteración 4",
    )
    plan = plan.replace(
        "**Totales del catálogo del plan:** 2014 registros Oxford 5000 + 999 registros Phrase List = 3013 registros; 2014 + 998 = 3012 unidades únicas. Se mantienen los 265 IDs de sesión y la secuencia de 253 sesiones léxicas A1–C1 más 12 sesiones C2 de integración/repaso. No se modifica la distribución ni los repasos C2 existentes.",
        "**Totales de la línea base de la iteración 9:** 2014 registros Oxford 5000 + 999 registros Phrase List = 3013 registros; 2014 + 998 = 3012 unidades únicas. La iteración 10 preserva esas 265 sesiones y sus repasos C2; añade las sesiones y unidades Oxford 3000 documentadas en el análisis cuantitativo v10.",
    )
    (OUT / "1_plan_estudio_por_sesiones_de_repeticion.md").write_text(
        plan.rstrip() + "\n\n" + addon_text, encoding="utf-8", newline="\n"
    )

    with (OUT / "2_catalogo_trazabilidad_fuentes.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as stream:
        writer = csv.DictWriter(
            stream, fieldnames=fields, delimiter=";", quotechar='"', lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(old_rows)
        writer.writerows(new_catalog)

    manifest_fields = [
        "id_sesion", "nivel_cefr", "orden_en_ampliacion_nivel", "tipo_sesion",
        "orden_global_suplemento",
        "objetivo_comunicativo", "vocabulario_foco", "gramatica_foco",
        "vocabulario_en_repaso", "unidades_nuevas", "eventos_unidad_repaso",
        "pares_nuevos", "pares_repaso", "pares_gramatica", "pares_integracion",
        "total_pares", "cohortes_fuente_repasadas",
    ]
    with (OUT / "3_sesiones_oxford3000.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=manifest_fields,
            delimiter=";",
            quotechar='"',
            lineterminator="\n",
        )
        writer.writeheader()
        for session in sessions:
            writer.writerow(
                {
                    "id_sesion": session["id"],
                    "nivel_cefr": session["level"],
                    "orden_en_ampliacion_nivel": session["local_index"],
                    "tipo_sesion": session["kind"],
                    "orden_global_suplemento": session["global_order"],
                    "objetivo_comunicativo": session["objective"],
                    "vocabulario_foco": session["focus"],
                    "gramatica_foco": session["grammar"],
                    "vocabulario_en_repaso": session["review"],
                    "unidades_nuevas": session["new_count"],
                    "eventos_unidad_repaso": session["review_count"],
                    "pares_nuevos": session["pairs_new"],
                    "pares_repaso": session["pairs_review"],
                    "pares_gramatica": session["pairs_grammar"],
                    "pares_integracion": session["pairs_integration"],
                    "total_pares": session["total"],
                    "cohortes_fuente_repasadas": session["cohorts"],
                }
            )

    print("SOURCE", len(records), counts, "unique printed head labels", len({r["head"] for r in records}))
    print(
        "PARTIAL overlaps by level",
        [
            (
                lev,
                sum(
                    r["level"] == lev
                    and (
                        bool(related.get((r["level"], r["page"], r["line_start"])))
                        or norm(r["head"]) == "phone"
                    )
                    for r in records
                ),
            )
            for lev in LEVELS
        ],
    )
    print(
        "SESSIONS",
        len(sessions),
        [
            (
                lev,
                sum(s["level"] == lev and s["new_count"] for s in sessions),
                sum(s["level"] == lev and not s["new_count"] for s in sessions),
            )
            for lev in LEVELS
        ],
    )
    print(
        "PAIR TOTALS",
        [
            sum(s[k] for s in sessions)
            for k in ("pairs_new", "pairs_review", "pairs_grammar", "pairs_integration")
        ],
    )
    old_session_refs = {
        row["sesion_plan"] for matches in related.values() for row in matches
    } | {phone_phrase[0]["sesion_plan"]}
    print("PREEXISTING RELATED SESSIONS", len(old_session_refs), sorted(old_session_refs))
    print("FILES", [(p.name, p.stat().st_size) for p in OUT.iterdir() if p.is_file()])


if __name__ == "__main__":
    main()
