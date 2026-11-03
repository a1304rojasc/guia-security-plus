# Guía de estudio CompTIA Security+ (SY0-701)

Guía en español para preparar el examen **CompTIA Security+ SY0-701**: resúmenes por dominio, glosario, 200 preguntas de práctica y un quiz que funciona sin conexión.

> ⚠️ **Aviso:** este material **no es oficial** y no está afiliado, respaldado ni revisado por CompTIA. «CompTIA» y «Security+» son marcas de CompTIA, Inc. Las preguntas son originales, no proceden de exámenes reales. Consulta siempre los objetivos oficiales en [comptia.org](https://www.comptia.org/certifications/security).

## Contenido

| Ruta | Qué es |
|---|---|
| [`dominios/1-conceptos-generales.md`](dominios/1-conceptos-generales.md) | 1. Conceptos generales de seguridad (12 %) |
| [`dominios/2-amenazas-vulnerabilidades-mitigaciones.md`](dominios/2-amenazas-vulnerabilidades-mitigaciones.md) | 2. Amenazas, vulnerabilidades y mitigaciones (22 %) |
| [`dominios/3-arquitectura-seguridad.md`](dominios/3-arquitectura-seguridad.md) | 3. Arquitectura de seguridad (18 %) |
| [`dominios/4-operaciones-seguridad.md`](dominios/4-operaciones-seguridad.md) | 4. Operaciones de seguridad (28 %) |
| [`dominios/5-gestion-supervision-programa.md`](dominios/5-gestion-supervision-programa.md) | 5. Gestión y supervisión del programa de seguridad (20 %) |
| [`glosario.md`](glosario.md) | Casi 200 términos con sigla en inglés, significado y dominio |
| [`preguntas/preguntas.json`](preguntas/preguntas.json) | 200 preguntas (24 / 44 / 36 / 56 / 40 por dominio) |
| [`quiz/index.html`](quiz/index.html) | Quiz interactivo autocontenido |
| `herramientas/` | `validar.py` (comprueba el banco) y `construir_quiz.py` (genera el quiz) |

Cada archivo de dominio sigue los objetivos oficiales (N.1, N.2…), con tablas comparativas, ejemplos y una sección final **«Trampas típicas del examen»**.

## Cómo usar la guía

1. Lee un dominio (`dominios/`) y marca lo que no entiendas.
2. Busca los términos nuevos en el `glosario.md`.
3. Practica en el quiz solo ese dominio y lee **todas** las explicaciones, también las de las preguntas acertadas.
4. Usa **«Repasar falladas»** hasta dejar la lista vacía.
5. Cuando lleves todos los dominios, haz el **modo examen** (90 preguntas, 90 minutos).

## Cómo abrir el quiz

- **En línea:** https://a1304rojasc.github.io/guia-security-plus/quiz/ (publicado con GitHub Pages).
- **Sin instalar nada:** descarga el repositorio (*Code → Download ZIP*) y abre `quiz/index.html` con doble clic. Funciona sin conexión y en el móvil.
- **Funciones:** elegir dominios y número de preguntas; preguntas y opciones mezcladas en cada intento; explicación tras cada respuesta; puntuación por dominio; modo examen con temporizador y explicaciones al final; repaso de falladas; tema claro/oscuro.
- **Teclado:** `1`–`4` o `A`–`D` para responder, flechas para moverse entre opciones, `Intro` para continuar.
- El progreso (estadísticas, falladas, sesión en curso) se guarda en el navegador (`localStorage`). En modo privado puede no conservarse.

### Si modificas las preguntas

```bash
python herramientas/validar.py         # comprueba el banco
python herramientas/construir_quiz.py  # regenera quiz/index.html
pip install pytest && pytest -q        # ejecuta los tests
```

GitHub Actions ejecuta el validador y los tests en cada push, y comprueba que `quiz/index.html` esté regenerado.

## Plan de estudio de 6 semanas

Unas 6–8 horas por semana. Los dominios con más peso tienen más tiempo.

| Semana | Estudio | Práctica en el quiz |
|---|---|---|
| 1 | Dominio 1 completo + inicio del glosario | Dominio 1 (24 preguntas). Repasar falladas |
| 2 | Dominio 2 (2.1–2.5) | Dominio 2 en dos bloques de 22 |
| 3 | Dominio 3 (3.1–3.4); memorizar tablas de RAID, backups y sitios | Dominio 3 + repaso mixto 1–2 |
| 4 | Dominio 4 (4.1–4.5) | 30 preguntas del dominio 4 |
| 5 | Dominio 4 (4.6–4.9) y dominio 5 completo; practicar ALE/SLE y RTO/RPO | Dominio 4 restante + dominio 5 |
| 6 | Repaso de todas las «Trampas típicas del examen» y del glosario | 2 simulacros en modo examen (objetivo ≥ 85 %) + repasar falladas hasta vaciar la lista |

Consejos: el examen real tiene hasta 90 preguntas (opción múltiple y de rendimiento/PBQ), 90 minutos y se aprueba con 750 sobre 900. Lee la pregunta entera: palabras como **«mejor»**, **«primero»** o **«más adecuado»** cambian la respuesta.

## Verificación de los objetivos oficiales

Los cinco dominios, sus pesos y los subdominios **1.1–5.6** se basan en el documento oficial *CompTIA Security+ SY0-701 Exam Objectives (versión 5.0)*. Durante la elaboración (noviembre de 2026) se verificaron por búsqueda web los pesos de los dominios y los títulos de varios objetivos (p. ej. 1.4, 3.1 y 4.9). **No se pudo descargar el PDF oficial completo** desde este entorno, así que el resto de títulos de objetivos procede del conocimiento del documento oficial y no se ha contrastado línea a línea. Compáralos con el PDF de CompTIA antes del examen.

| Dominio | Objetivos |
|---|---|
| 1 | 1.1 Controles · 1.2 Conceptos fundamentales · 1.3 Gestión de cambios · 1.4 Criptografía |
| 2 | 2.1 Actores · 2.2 Vectores y superficies · 2.3 Vulnerabilidades · 2.4 Indicadores de actividad maliciosa · 2.5 Mitigaciones |
| 3 | 3.1 Modelos de arquitectura · 3.2 Infraestructura empresarial · 3.3 Protección de datos · 3.4 Resiliencia y recuperación |
| 4 | 4.1 Técnicas sobre recursos · 4.2 Gestión de activos · 4.3 Gestión de vulnerabilidades · 4.4 Alertas y monitorización · 4.5 Mejorar capacidades · 4.6 IAM · 4.7 Automatización · 4.8 Respuesta a incidentes · 4.9 Fuentes de datos |
| 5 | 5.1 Gobernanza · 5.2 Gestión de riesgos · 5.3 Riesgo de terceros · 5.4 Cumplimiento · 5.5 Auditorías y evaluaciones · 5.6 Concienciación |
