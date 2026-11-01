# Informe de revisión — `frases_y_expresiones.csv`

## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Recuento real |
|---|---|---|---:|
| `frases_y_expresiones.csv` | Observado | Ninguna de las reglas generales comprobables en el CSV | 151 frases (mínimo: 150) |

## `frases_y_expresiones.csv` — Observado

**Reglas generales por archivo incumplidas**

- Ninguna de las reglas generales comprobables en el CSV. La lectura UTF-8 fue válida; las 151 filas tienen dos campos separados por `;`, no hay filas vacías ni texto corrupto, y se cumple el mínimo de 150 frases.
- **Cobertura:** no evaluada; no se proporcionó el plan y no se infieren IDs ni sesiones.

**Reglas incumplidas por línea**

- **Fila 103 — Regla: Frase con sentido.** «Mi padre está por teléfono ahora» no suena natural en español. Reemplazar por: `Mi padre está hablando por teléfono ahora.;My father is on the phone now.`
- **Fila 139 — Regla: Desambiguación de sujeto.** «Trabajaron juntos durante muchos años» no identifica inequívocamente «they»; también puede referirse a «ustedes» en trato formal. Reemplazar por: `Ellos trabajaron juntos durante muchos años.;They worked together for many years.`
- **Fila 148 — Regla: Frase con sentido.** «Para felicitarla» no especifica que se trata de desearle un feliz cumpleaños, como sí lo hace la traducción inglesa. Reemplazar por: `Hablé por teléfono con mi tía para desearle un feliz cumpleaños.;I talked to my aunt on the phone to wish her a happy birthday.`

**Sesiones completadas:** ninguna; este archivo queda observado.
