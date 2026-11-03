# Dominio 5 · Gestión y supervisión del programa de seguridad (20 %)

> Objetivos oficiales SY0-701: 5.1 – 5.6. Unas 18 preguntas del examen real.

---

## 5.1 Elementos de una gobernanza de seguridad eficaz

### Documentos
| Documento | Qué es | Obligatorio |
|---|---|---|
| Política (policy) | Declaración de alto nivel de intenciones | Sí |
| Estándar (standard) | Requisitos concretos (p. ej. AES-256, contraseñas ≥ 12) | Sí |
| Procedimiento (procedure) | Pasos detallados (cómo hacerlo) | Sí |
| Guía (guideline) | Recomendación | **No** |

**Políticas típicas:** uso aceptable (AUP), seguridad de la información, continuidad de negocio, recuperación ante desastres, respuesta a incidentes, SDLC, gestión de cambios.
**Estándares:** contraseñas, gestión de accesos, seguridad física, cifrado.
**Procedimientos:** gestión de cambios, incorporación/salida de personal (onboarding/offboarding), playbooks.

**Consideraciones externas:** regulatorias, legales, sectoriales, locales/regionales/nacionales/globales.
**Supervisión:** auditorías, revisiones periódicas.
**Estructuras de gobernanza:** juntas (boards), comités, entidades gubernamentales, centralizada/descentralizada.

### Roles sobre los datos
| Rol | Responsabilidad |
|---|---|
| Propietario (owner) | Responsable final; decide la clasificación (alto cargo) |
| Responsable del tratamiento (controller) | Decide **por qué y cómo** se tratan los datos personales |
| Encargado del tratamiento (processor) | Trata datos **en nombre** del controller |
| Custodio (custodian) / administrador (steward) | Custodio: implementa controles técnicos (TI). Steward: calidad y uso correcto del dato |

---

## 5.2 Proceso de gestión de riesgos

**Identificación → Evaluación → Análisis → Registro → Tolerancia/apetito → Estrategias → Informes.**

### Evaluación (assessment)
Ad hoc, recurrente, puntual (one-time), continua.

### Análisis cuantitativo
| Fórmula | Significado |
|---|---|
| **SLE = AV × EF** | Pérdida por un incidente = valor del activo × factor de exposición (%) |
| **ALE = SLE × ARO** | Pérdida anual = SLE × tasa de ocurrencia anual |

**Ejemplo:** servidor de 50 000 €, un incendio destruiría el 40 % (EF = 0,4) → SLE = 20 000 €. Si ocurre una vez cada 10 años (ARO = 0,1) → ALE = 2 000 €/año. Un control que cueste más de 2 000 €/año no compensa.

**Análisis cualitativo:** probabilidad × impacto (alto/medio/bajo), matriz de calor.

### Registro de riesgos (risk register)
Lista de riesgos, **indicadores clave de riesgo (KRI)**, **propietarios del riesgo**, **umbral de riesgo (risk threshold)**.

**Tolerancia al riesgo (risk tolerance)** y **apetito de riesgo (risk appetite)**: expansivo, conservador, neutral.

### Estrategias de gestión del riesgo
| Estrategia | Ejemplo |
|---|---|
| Transferir (transfer) | Contratar un ciberseguro |
| Aceptar (accept) | El coste del control supera el impacto. Variantes: **exención (exemption)** y **excepción (exception)** |
| Evitar (avoid) | Dejar de ofrecer el servicio arriesgado |
| Mitigar (mitigate) | Aplicar controles para reducirlo |

**Riesgo inherente** (antes de controles) vs **riesgo residual** (después).

### Análisis de impacto en el negocio (BIA)
| Métrica | Significado | Ejemplo |
|---|---|---|
| **RTO** (Recovery Time Objective) | Tiempo máximo aceptable para restaurar el servicio | "La tienda online debe volver en 4 h" |
| **RPO** (Recovery Point Objective) | Máxima pérdida de datos aceptable (en tiempo) | "Podemos perder como mucho 1 h de pedidos" → backups cada hora |
| **MTTR** (Mean Time To Repair) | Tiempo medio de reparación | 2 h para cambiar un disco |
| **MTBF** (Mean Time Between Failures) | Tiempo medio entre fallos (fiabilidad) | Un disco falla cada 100 000 h |

---

## 5.3 Evaluación y gestión de riesgos de terceros

- **Evaluación de proveedores:** pruebas de penetración, **derecho a auditar (right-to-audit clause)**, evidencia de auditorías internas, auditorías independientes, análisis de la cadena de suministro.
- **Selección:** diligencia debida (due diligence), conflictos de interés.
- **Acuerdos:**

| Acuerdo | Qué define |
|---|---|
| SLA (Service Level Agreement) | Niveles de servicio medibles (disponibilidad 99,9 %) |
| MOA / MOU | Acuerdo / memorando de entendimiento (menos formal) |
| MSA (Master Service Agreement) | Contrato marco con términos generales |
| WO / SOW (Work Order / Statement of Work) | Trabajo concreto, entregables, plazos |
| NDA | Confidencialidad |
| BPA (Business Partners Agreement) | Relación entre socios (reparto de beneficios, responsabilidades) |

- **Monitorización de proveedores**, **cuestionarios**, **reglas de compromiso (rules of engagement)**.

---

## 5.4 Elementos de un cumplimiento (compliance) de seguridad eficaz

- **Informes de cumplimiento:** internos y externos.
- **Consecuencias del incumplimiento:** multas, sanciones, daño reputacional, pérdida de licencia, impacto contractual.
- **Monitorización del cumplimiento:** diligencia debida/cuidado debido (due diligence/due care), atestación y reconocimiento (attestation and acknowledgement), automatización.
- **Privacidad:** leyes locales/regionales/nacionales/globales (p. ej. **GDPR/RGPD**), **sujeto de los datos (data subject)**, controller vs processor, propiedad, **inventario y retención de datos**, **derecho al olvido (right to be forgotten)**.

---

## 5.5 Tipos y procesos de auditorías y evaluaciones

- **Atestación (attestation):** declaración formal de que algo se cumple.
- **Interna:** cumplimiento, comité de auditoría, autoevaluaciones.
- **Externa:** reguladores, exámenes, evaluaciones, auditores independientes (p. ej. SOC 2).

### Pruebas de penetración (penetration testing)
| Tipo / concepto | Descripción |
|---|---|
| Físico | Intentar entrar en las instalaciones |
| Ofensivo (red team) | Ataca |
| Defensivo (blue team) | Defiende |
| Integrado (purple team) | Red + blue colaborando |
| Entorno conocido (known environment, antes white box) | El auditor tiene toda la información |
| Entorno parcialmente conocido (partially known, gray box) | Información parcial |
| Entorno desconocido (unknown environment, black box) | Sin información, como un atacante externo |

**Reconocimiento:** pasivo (OSINT, sin tocar el objetivo) vs activo (escaneo de puertos, interacción directa).

**Reglas de compromiso (rules of engagement):** alcance, horario, contactos, qué está prohibido. Se acuerdan **antes** de la prueba.

---

## 5.6 Implementar prácticas de concienciación en seguridad (escenarios)

- **Campañas de phishing:** reconocer intentos, responder a mensajes reportados/sospechosos, simulaciones.
- **Reconocer comportamientos anómalos:** riesgoso, inesperado, no intencionado.
- **Formación de usuarios:** guías y políticas, amenazas internas, gestión de contraseñas, medios extraíbles y cables, conciencia situacional, seguridad operativa, entornos híbridos/remotos, ingeniería social.
- **Informes y monitorización:** iniciales y recurrentes.
- **Desarrollo y ejecución** del programa.

**Ejemplo:** tras una simulación de phishing, el 18 % hace clic. Se asigna formación breve a quienes hicieron clic y se repite la campaña en 3 meses para medir la mejora.

---

## Trampas típicas del examen
- **RPO = datos** (cuántos puedo perder); **RTO = tiempo** (cuándo vuelvo). MTBF alto = más fiable.
- **ALE = SLE × ARO**; **SLE = AV × EF**. Un ARO de "una vez cada 5 años" = 0,2.
- **Ciberseguro = transferir**, no mitigar.
- **Guía** no es obligatoria; política, estándar y procedimiento sí.
- **Controller decide**, **processor ejecuta** por cuenta del controller.
- **Unknown environment** = black box; **known** = white box.
- **Reconocimiento pasivo** no interactúa con los sistemas del objetivo.
- **Rules of engagement** se firman antes de empezar el pentest.
- **SLA** mide el servicio; **NDA** protege la confidencialidad; **SOW** describe el trabajo concreto.
- **Right-to-audit** es una cláusula contractual con el proveedor.
- **Riesgo residual** = lo que queda tras aplicar controles.
