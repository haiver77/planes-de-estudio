# Método de cotejo y localizadores — iteración 12

## Fuente y referencia inmutable

Fuente cotejada: `resources/Oxford 3000_by CEFR level.pdf`. SHA-256:
`a1ccae422ddda0011e4783ce60a1d67c05a276a806dd07c2d3d887f4d97c5a8c`.
El hash se repite en el catálogo, en el campo `sha256_pdf_fuente`. Si el hash del
PDF disponible no coincide, no se deben dar por válidas las coordenadas hasta
repetir el cotejo con esa versión.

## Localizador primario

Para las 3.306 filas O3K, el catálogo conserva las columnas heredadas de página
y líneas extraídas, pero estas líneas quedan como referencia auxiliar, no como
localizador primario. Se agregan:

- `elemento_pdf_estable`: ordinal de entrada dentro de la página,
  `O3K-P{página}-E{índice}`. El índice se calcula ordenando las entradas por
  bandas de columna visual de izquierda a derecha y, dentro de cada columna,
  por `y0` y luego `x0` ascendentes. Para reproducir las bandas, ordenar los
  `x0` de todas las cajas de la página; iniciar la primera banda con el primer
  valor. Cada valor siguiente inicia una nueva banda si supera en más de 20
  puntos el centro actual; si no, se incorpora y el centro pasa a ser la media
  aritmética del centro anterior y el nuevo valor. Numerar las entradas desde
  1 dentro de cada página.
- `bbox_pdf_puntos`: coordenadas `x0,y0,x1,y1` en puntos PDF, con origen en la
  esquina superior izquierda de la página según PyMuPDF; valores redondeados a
  dos decimales.
- `localizador_pdf_estable`: combinación de fuente/hash, página, ordinal y caja
  de coordenadas.
- `metodo_cotejo_localizador`: indica si la caja procede de una línea/span
  exacto o de la unión de rectángulos encontrados por búsqueda literal.

La caja de una entrada que ocupa más de una línea es la unión de todos los
rectángulos de su coincidencia. Para las 12 entradas cuyo texto extraído no
coincide carácter por carácter entre pypdf y PyMuPDF, se coteja la cadena fuente
literal con `page.search_for(...)` en la página ya fijada por el catálogo; se
unen las cajas devueltas. No se usa un número de línea OCR para decidir qué
entrada es.

## Reproducción del cotejo

Con Python y PyMuPDF instalados, este procedimiento permite reproducir un
localizador:

```python
import hashlib
import pymupdf

pdf = "resources/Oxford 3000_by CEFR level.pdf"
raw = b"".join(open(pdf, "rb").readlines())
print(hashlib.sha256(raw).hexdigest())  # debe coincidir con sha256_pdf_fuente

doc = pymupdf.open(pdf)
page_number = 1  # tomar pagina_pdf del registro del catálogo; empieza en 1
source_text = "April n."  # tomar entrada_fuente_raw_pypdf, sin alterarla
page = doc[page_number - 1]

exact_lines = []
for block in page.get_text("dict")["blocks"]:
    for line in block.get("lines", []):
        text = "".join(span["text"] for span in line["spans"]).strip()
        if text == source_text.strip():
            exact_lines.append(line["bbox"])

if exact_lines:
    boxes = exact_lines
else:
    boxes = [tuple(rect) for rect in page.search_for(source_text)]

assert boxes, "No se encontró el texto: cotejar la transcripción antes de usarlo"
box = (
    min(b[0] for b in boxes), min(b[1] for b in boxes),
    max(b[2] for b in boxes), max(b[3] for b in boxes),
)
print(page_number, tuple(round(v, 2) for v in box))
```

La igualdad de una línea completa es sensible a mayúsculas y sirve para
corroborar formas como `I`, `CD`, `DVD`, `OK`, `T-shirt`, `TV` e `IT`. La
búsqueda literal de respaldo puede devolver coincidencias de subcadena (por
ejemplo, `IT` dentro de `limit`); por eso no se acepta una coincidencia por
sí sola: se combina la página del registro, el texto de entrada completo y la
comprobación visual de la caja. Las formas de las 26 entradas corregidas se
muestran en `7_evidencia_visual_capitalizacion.pdf`.

La clave técnica se calcula como
`" ".join(NFKC(entrada_normalizada).split()).casefold()`. Para las 26 grafías,
esta clave coincide con la clave en minúsculas previa a la corrección; por ello
se restauran las mayúsculas legibles sin alterar la identidad usada para
comparar ni las asignaciones de deduplicación heredadas.

## Cotejo visual y capitalización

`entrada_fuente_raw_pypdf` permanece literal. `entrada_normalizada` funciona
como forma legible y preserva la capitalización significativa restaurada. La
nueva columna `clave_comparacion_casefold` es una clave técnica separada para
comparar/deduplicar; no reemplaza ni sobrescribe la transcripción ni la forma
legible. Los identificadores canónicos, estados de deduplicación, niveles,
unidades y asignaciones de la iteración anterior se conservan.

Para una auditoría visual reproducible:

1. Abra `7_evidencia_visual_capitalizacion.pdf` y localice la tarjeta por
   `registro_fuente`.
2. Compare la grafía visible y el uso de mayúsculas con el texto fuente de la
   tarjeta; su rótulo incluye la página y la caja de coordenadas.
3. Abra la página indicada del PDF original y repita el cotejo usando la caja
   del catálogo. Las coordenadas se expresan en puntos PDF, no en píxeles.
4. Compruebe `sha256_pdf_fuente` antes de reutilizar coordenadas con otra copia
   del PDF.

Las referencias de línea heredadas se mantienen para no borrar procedencia,
pero no deben usarse como sustituto del localizador página + ordinal + caja.
