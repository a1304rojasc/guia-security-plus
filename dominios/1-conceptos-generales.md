# Dominio 1 · Conceptos generales de seguridad (12 %)

> Objetivos oficiales SY0-701: 1.1 – 1.4. Unas 9–11 preguntas del examen real.

---

## 1.1 Comparar y contrastar tipos de controles de seguridad (security controls)

Un control se clasifica **dos veces**: por **categoría** (quién/cómo se implementa) y por **tipo** (qué efecto tiene).

### Categorías

| Categoría | Qué es | Ejemplos |
|---|---|---|
| Técnico (technical) | Implementado por sistemas, hardware o software | Firewall, cifrado, MFA, antivirus, ACL |
| Gerencial (managerial) | Decisiones de gestión, políticas, evaluación de riesgos | Política de seguridad, evaluación de riesgos, planificación |
| Operacional (operational) | Lo ejecutan **personas** en el día a día | Guardias, formación de concienciación, gestión de cambios |
| Físico (physical) | Limitan el acceso físico | Cerraduras, vallas, bolardos (bollards), CCTV |

### Tipos

| Tipo | Función | Ejemplo |
|---|---|---|
| Preventivo (preventive) | Evita que ocurra el incidente | Firewall que bloquea, cerradura, política de contraseñas |
| Disuasorio (deterrent) | Desanima al atacante, no lo impide | Cartel "zona vigilada", banner de inicio de sesión |
| Detectivo (detective) | Identifica/registra el incidente | IDS, logs, CCTV revisado, auditoría |
| Correctivo (corrective) | Reduce el impacto y restaura tras el incidente | Restaurar backups, parchear, reinstalar |
| Compensatorio (compensating) | Sustituye a un control que no se puede aplicar | Segmentar un sistema legacy que no admite parches |
| Directivo (directive) | Indica lo que se debe hacer | Política "cifrar portátiles", procedimiento, señalética de obligación |

**Ejemplo combinado:** una cámara CCTV es *física* y, según el contexto, *detectiva* (graba) o *disuasoria* (visible).

---

## 1.2 Conceptos fundamentales de seguridad

### Tríada CIA
- **Confidencialidad (confidentiality):** solo quien debe, ve. → cifrado, control de acceso.
- **Integridad (integrity):** los datos no se alteran sin autorización. → hashing, firmas digitales.
- **Disponibilidad (availability):** acceso cuando se necesita. → redundancia, backups, balanceo.

### No repudio (non-repudiation)
El emisor no puede negar haber enviado algo → **firma digital** (clave privada del emisor).

### AAA (Authentication, Authorization, Accounting)
| Paso | Pregunta | Ejemplo |
|---|---|---|
| Identificación | ¿Quién dices ser? | Nombre de usuario |
| Autenticación (authentication) | ¿Lo puedes probar? | Contraseña, certificado, biometría |
| Autorización (authorization) | ¿Qué puedes hacer? | Permisos, roles |
| Contabilidad (accounting) | ¿Qué hiciste? | Logs, RADIUS accounting |

Autenticación de **sistemas/dispositivos**: certificados en el equipo, CA interna, 802.1X. Modelos de autorización: ver 4.6.

### Análisis de brechas (gap analysis)
Compara el estado actual con el deseado (p. ej. con NIST CSF o ISO 27001) y produce un plan para cerrar la diferencia.

### Confianza cero (Zero Trust)
"Nunca confíes, verifica siempre". Divide en dos planos:

| Plano | Componentes |
|---|---|
| Plano de control (control plane) | Autenticación adaptativa (adaptive identity), reducción del alcance de amenazas (threat scope reduction), acceso basado en políticas (policy-driven access control), **motor de políticas (Policy Engine)** que decide, **administrador de políticas (Policy Administrator)** que comunica la decisión |
| Plano de datos (data plane) | Zona implícitamente confiable (implicit trust zones), sujeto/sistema (subject/system), **punto de aplicación de políticas (PEP, Policy Enforcement Point)** |

### Seguridad física
Bolardos (bollards), vestíbulo de control de acceso (access control vestibule, antes "mantrap"), vallas, videovigilancia, guardias, tarjetas de acceso, iluminación, sensores (infrarrojos, presión, microondas, ultrasónicos).

### Tecnología de engaño (deception and disruption)
| Término | Qué es |
|---|---|
| Honeypot | Sistema señuelo para atraer y estudiar atacantes |
| Honeynet | Red de honeypots |
| Honeyfile | Archivo señuelo (p. ej. "contraseñas.xlsx") que dispara alerta al abrirse |
| Honeytoken | Dato falso (credencial, registro) cuyo uso delata al intruso |

---

## 1.3 Gestión de cambios (change management) y su impacto en la seguridad

**Procesos de negocio:** aprobación (approval process), propiedad (ownership), partes interesadas (stakeholders), análisis de impacto (impact analysis), pruebas (test results), plan de reversión (backout plan), ventana de mantenimiento (maintenance window), procedimiento operativo estándar (SOP).

**Implicaciones técnicas:** listas de permitidos/denegados (allow/deny lists), actividades restringidas, tiempo de inactividad (downtime), reinicio de servicios/aplicaciones, aplicaciones heredadas (legacy), dependencias.

**Documentación y control de versiones:** actualizar diagramas, políticas y procedimientos tras el cambio; control de versiones (version control).

**Ejemplo:** un parche de base de datos se prueba en un entorno de pruebas, el CAB (Change Advisory Board) lo aprueba, se aplica en la ventana del domingo 02:00 y existe un plan de reversión (restaurar snapshot) si falla.

---

## 1.4 Importancia de usar soluciones criptográficas apropiadas

### PKI (infraestructura de clave pública)
- **Clave pública** (se comparte) / **clave privada** (nunca se comparte).
- **Depósito de claves (key escrow):** un tercero guarda copia de claves para recuperación.
- **CA (Certificate Authority)** emite certificados; **RA** verifica identidades.
- **CRL** (lista de revocación) vs **OCSP** (consulta en tiempo real); **OCSP stapling**: el servidor adjunta la respuesta OCSP.
- **CSR (Certificate Signing Request):** solicitud que genera el propio sujeto con su clave pública.
- **Certificado comodín (wildcard)** `*.ejemplo.com`; **SAN** permite varios nombres.
- **Autofirmado (self-signed)** vs de terceros; **raíz de confianza (root of trust)**.

### Simétrico vs asimétrico

| | Simétrico | Asimétrico |
|---|---|---|
| Claves | Una compartida | Par pública/privada |
| Velocidad | Rápido | Lento |
| Uso típico | Cifrar datos en volumen | Intercambio de claves, firmas digitales |
| Algoritmos | AES, 3DES (obsoleto), ChaCha20 | RSA, ECC, Diffie-Hellman (DH/ECDHE) |
| Problema | Distribuir la clave | Coste computacional |

En la práctica se combinan (cifrado híbrido): TLS usa asimétrico para acordar una clave de sesión simétrica.

### Niveles de cifrado
Disco completo (FDE), partición, volumen, archivo, base de datos, registro (record), transporte (TLS, IPsec).

### Herramientas
| Herramienta | Qué hace |
|---|---|
| TPM (Trusted Platform Module) | Chip en la placa; guarda claves, arranque medido, BitLocker |
| HSM (Hardware Security Module) | Dispositivo dedicado para gestionar claves a gran escala |
| KMS (Key Management System) | Gestión centralizada de claves (a menudo en la nube) |
| Enclave seguro (secure enclave) | Zona aislada del procesador para datos sensibles |

### Otros conceptos
- **Hashing:** resumen de tamaño fijo, unidireccional. SHA-256 (seguro), MD5/SHA-1 (débiles, colisiones).
- **Salting (sal):** valor aleatorio añadido a la contraseña antes del hash → evita tablas arcoíris (rainbow tables).
- **Estiramiento de claves (key stretching):** PBKDF2, bcrypt → hash repetido para hacer lenta la fuerza bruta.
- **Firmas digitales:** hash del mensaje cifrado con la **clave privada del emisor**; se verifica con su pública. Dan integridad, autenticación y no repudio.
- **Ofuscación (obfuscation):** esteganografía (ocultar datos en imágenes), tokenización (sustituir dato por token sin valor), enmascaramiento de datos (data masking, `****1234`).
- **Blockchain / libro mayor abierto (open public ledger).**
- **Intercambio de claves (key exchange):** Diffie-Hellman.

### ¿Qué clave uso? (muy preguntado)
| Objetivo | Clave |
|---|---|
| Cifrar para que solo Bob lea | Pública de **Bob** |
| Bob descifra | Privada de **Bob** |
| Alice firma | Privada de **Alice** |
| Verificar firma de Alice | Pública de **Alice** |

---

## Trampas típicas del examen
- **Disuasorio ≠ preventivo:** un cartel no impide nada; una cerradura sí.
- **Compensatorio** aparece cuando el escenario dice "no se puede aplicar el control principal".
- **Política de seguridad** = control *gerencial* + tipo *directivo*. La **formación** es *operacional*.
- Firmar = clave **privada del emisor**; cifrar confidencialmente = clave **pública del receptor**.
- **Hash ≠ cifrado:** el hash no se "descifra". Integridad ≠ confidencialidad.
- **Salt** combate rainbow tables; **key stretching** combate fuerza bruta.
- **OCSP** es en tiempo real; la **CRL** se descarga periódicamente.
- **TPM** va en el equipo; **HSM** es un dispositivo dedicado de alto rendimiento.
- **Tokenización** reemplaza el dato (no es reversible matemáticamente); el **cifrado** sí es reversible con la clave.
- En Zero Trust, quien **decide** es el Policy Engine; quien **aplica** es el PEP.
