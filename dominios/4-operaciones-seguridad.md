# Dominio 4 · Operaciones de seguridad (28 %)

> Objetivos oficiales SY0-701: 4.1 – 4.9. Es el dominio con más peso (~25 preguntas).

---

## 4.1 Aplicar técnicas de seguridad comunes a los recursos informáticos (escenarios)

- **Líneas base seguras (secure baselines):** establecer → desplegar → mantener. Ej.: CIS Benchmarks, GPO.
- **Objetivos de bastionado (hardening targets):** móviles, estaciones de trabajo, switches, routers, nube, servidores, ICS/SCADA, embebidos, RTOS, IoT.

### Inalámbrico
| Elemento | Recomendación |
|---|---|
| Estudio de sitio (site survey) / mapa de calor (heat map) | Ubicar APs y detectar interferencias / APs falsos |
| WPA3 | Usa **SAE** (Simultaneous Authentication of Equals) en lugar de PSK |
| WPA2/WPA3-Enterprise | 802.1X + RADIUS, credenciales por usuario |
| WEP / WPS | Inseguros → deshabilitar |

**AAA/RADIUS** para autenticación inalámbrica; **EAP** y sus variantes (EAP-TLS = certificados en ambos extremos).

### Móviles
| Modelo | Propiedad | Control |
|---|---|---|
| BYOD | Empleado | Bajo; usar contenedorización / MAM |
| COPE | Empresa, uso personal permitido | Alto |
| CYOD | Empresa, el empleado elige entre una lista | Alto |

**MDM** (gestión de dispositivos móviles): borrado remoto, cifrado, bloqueo, geocercas (geofencing).
Conectividad: celular, Wi-Fi, Bluetooth.

### Seguridad de aplicaciones
Validación de entradas (input validation), cookies seguras (Secure, HttpOnly), análisis estático (SAST), firma de código (code signing), **sandboxing**, monitorización.

---

## 4.2 Gestión de activos de hardware, software y datos

| Fase | Claves |
|---|---|
| Adquisición / compras | Proceso aprobado, proveedores evaluados |
| Asignación / contabilidad | Propietario (ownership), clasificación |
| Monitorización / seguimiento | Inventario, enumeración |
| Eliminación / desmantelamiento | Saneamiento (sanitization), destrucción, **certificado de destrucción**, retención de datos |

**Saneamiento de medios:**
| Método | Nota |
|---|---|
| Sobrescritura (overwrite / wiping) | Reutilizable el disco |
| Desmagnetización (degaussing) | Discos magnéticos; **no sirve en SSD** |
| Borrado criptográfico (crypto erase) | Destruir la clave de cifrado; ideal en SSD |
| Destrucción física | Triturar, incinerar, pulverizar |

---

## 4.3 Actividades de gestión de vulnerabilidades

### Identificación
Escaneo de vulnerabilidades, análisis de aplicaciones (estático/SAST, dinámico/DAST, revisión de paquetes), **fuentes de inteligencia de amenazas (threat feeds)**: OSINT, propietarias, ISAC, **dark web**, pruebas de penetración, **programa de recompensas (bug bounty)**, auditoría del sistema.

### Análisis
| Concepto | Descripción |
|---|---|
| Confirmación | Verdadero positivo / falso positivo / falso negativo |
| Priorización | Según criticidad y exposición |
| **CVSS** | Puntuación 0–10 de gravedad |
| **CVE** | Identificador público de vulnerabilidad (CVE-2024-1234) |
| Clasificación | Tipo de vulnerabilidad |
| Exposición, entorno, impacto, tolerancia al riesgo | Contexto de la organización |

**Falso positivo** = alerta de algo que no existe. **Falso negativo** = no se detecta algo que sí existe (más peligroso).

### Respuesta y remediación
Parcheo, seguro (insurance), segmentación, **controles compensatorios**, **excepciones y exenciones** (exceptions/exemptions).

### Validación
Re-escaneo (rescanning), auditoría, verificación. Después: **informes (reporting)**.

---

## 4.4 Conceptos y herramientas de alertas y monitorización

**Recursos monitorizados:** sistemas, aplicaciones, infraestructura.

**Actividades:** agregación de logs, alertas, escaneo, informes, archivado, respuesta a alertas (cuarentena, ajuste de alertas / alert tuning para reducir falsos positivos).

| Herramienta | Uso |
|---|---|
| SIEM | Centraliza y correlaciona logs; genera alertas |
| SCAP | Estándar para automatizar evaluación de configuración/vulnerabilidades |
| Benchmarks | CIS, guías del fabricante |
| Agentes / sin agente (agentless) | Recogida de datos |
| Antivirus | Firmas |
| DLP | Prevención de pérdida de datos |
| SNMP traps | Alertas de dispositivos de red |
| NetFlow | Metadatos de flujos de red (quién habla con quién, cuánto) |
| Escáner de vulnerabilidades | Detecta fallos conocidos |

---

## 4.5 Modificar capacidades empresariales para mejorar la seguridad (escenarios)

- **Firewall:** reglas, ACL, puertos/protocolos, zonas, regla implícita "denegar todo" (implicit deny) al final.
- **IDS/IPS:** firmas (signatures) vs tendencias/anomalías (trends).
- **Filtrado web:** basado en agente, proxy centralizado, URL scanning, categorías de contenido, reglas de bloqueo, reputación.
- **Seguridad del SO:** Group Policy, **SELinux** (control de acceso obligatorio).
- **Protocolos seguros:** usar protocolos y puertos seguros, transporte seguro.
- **Filtrado DNS.**
- **Seguridad de correo:**

| Mecanismo | Qué hace |
|---|---|
| SPF | Lista de servidores autorizados a enviar por el dominio (registro TXT) |
| DKIM | Firma digital de los correos del dominio |
| DMARC | Política de qué hacer si SPF/DKIM fallan + informes |
| Gateway de correo | Filtra spam/malware |

- **Monitorización de integridad de archivos (FIM).**
- **DLP**, **NAC**, **EDR/XDR**, **analítica de comportamiento de usuarios (UBA/UEBA)**.

### Puertos/protocolos seguros
| Inseguro | Seguro |
|---|---|
| Telnet 23 | SSH 22 |
| HTTP 80 | HTTPS 443 |
| FTP 20/21 | SFTP 22 / FTPS 989-990 |
| LDAP 389 | LDAPS 636 |
| SNMPv1/v2 161 | SNMPv3 |
| POP3 110 / IMAP 143 | POP3S 995 / IMAPS 993 |
| SMTP 25 | SMTPS/STARTTLS 465/587 |
| DNS 53 | DNSSEC (integridad), DoH/DoT |

---

## 4.6 Implementar y mantener la gestión de identidades y accesos (IAM)

- **Aprovisionamiento / desaprovisionamiento** de cuentas (deprovisioning al salir el empleado).
- **Prueba de identidad (identity proofing).**
- **Federación:** confiar en la identidad de otro dominio. **SSO** con **SAML** (XML, empresa), **OAuth** (autorización delegada), **OpenID Connect** (autenticación sobre OAuth), **LDAP** (directorio).
- **Interoperabilidad**, **atestación (attestation)**: revisión periódica de permisos.

### Modelos de control de acceso
| Modelo | Quién decide | Ejemplo |
|---|---|---|
| Obligatorio (MAC) | El sistema según etiquetas (secreto, alto secreto) | Militar, SELinux |
| Discrecional (DAC) | El **propietario** del recurso | Permisos NTFS que asigna el dueño |
| Basado en roles (RBAC) | El rol/puesto | "Contabilidad" accede a facturas |
| Basado en reglas (rule-based) | Reglas globales | Firewall, acceso solo de 8 a 18 h |
| Basado en atributos (ABAC) | Combinación de atributos (usuario, recurso, entorno) | "Médico + su planta + horario laboral" |
| Restricción horaria (time-of-day) | — | — |
| Mínimo privilegio | — | — |

### MFA: factores
| Factor | Ejemplo |
|---|---|
| Algo que sabes | Contraseña, PIN |
| Algo que tienes | Token, smartcard, app TOTP, llave de seguridad (FIDO2) |
| Algo que eres | Huella, rostro |
| Algún lugar donde estás | Geolocalización |

Dos contraseñas = **un solo factor**. Contraseñas: longitud, complejidad, reutilización, caducidad, gestores de contraseñas, **sin contraseña (passwordless)**.

### PAM (gestión de acceso privilegiado)
Acceso **justo a tiempo (JIT)**, **bóveda de contraseñas (password vaulting)**, **credenciales efímeras (ephemeral credentials)**.

---

## 4.7 Automatización y orquestación en operaciones seguras

**Casos de uso:** aprovisionamiento de usuarios y recursos, guardarraíles (guard rails), grupos de seguridad, creación de tickets, escalado, habilitar/deshabilitar servicios, integración continua y pruebas, integraciones y APIs.

| Beneficio | Riesgo / consideración |
|---|---|
| Eficiencia, ahorro de tiempo | Complejidad |
| Aplicar líneas base | Coste |
| Configuraciones estándar | **Punto único de fallo** |
| Escalar de forma segura | **Deuda técnica** |
| Retención de personal, tiempo de reacción | Soporte continuo |

**SOAR:** orquesta respuestas automáticas mediante playbooks.

---

## 4.8 Actividades de respuesta a incidentes

### Proceso (orden oficial)
1. **Preparación (preparation)**
2. **Detección (detection)**
3. **Análisis (analysis)**
4. **Contención (containment)**
5. **Erradicación (eradication)**
6. **Recuperación (recovery)**
7. **Lecciones aprendidas (lessons learned)**

**Formación** y **pruebas** (tabletop, simulación). **Análisis de causa raíz (root cause analysis)**. **Búsqueda de amenazas (threat hunting)**: proactiva.

### Forense digital
| Concepto | Descripción |
|---|---|
| Retención legal (legal hold) | Obligación de conservar datos ante un litigio |
| Cadena de custodia (chain of custody) | Registro de quién manejó la evidencia y cuándo |
| Adquisición | Copias bit a bit; verificar con hash |
| Informes | Documentar hallazgos |
| Preservación | Evitar alterar la evidencia |
| e-discovery | Recopilación de información electrónica para un proceso legal |

**Orden de volatilidad (de más a menos volátil):** registros/caché de CPU → RAM → estado de red/procesos → disco → logs remotos → backups/medios de archivo.

---

## 4.9 Usar fuentes de datos para apoyar una investigación (escenarios)

| Fuente | Qué aporta |
|---|---|
| Logs de firewall | IPs/puertos permitidos o bloqueados |
| Logs de aplicación | Errores, accesos a la app |
| Logs de endpoint | Eventos del equipo |
| Logs del SO | Inicios de sesión, servicios |
| Logs de IPS/IDS | Firmas detectadas |
| Logs de red | Switches, routers |
| Metadatos | Datos sobre los datos (cabeceras de correo, EXIF) |
| Escaneos de vulnerabilidades | Qué estaba expuesto |
| Paneles (dashboards) y salidas automáticas | Visión agregada |
| Captura de paquetes (packet capture, pcap) | Contenido completo del tráfico |

---

## Trampas típicas del examen
- Orden de respuesta: **contención antes que erradicación**; las lecciones aprendidas van al final.
- **Degaussing no funciona en SSD**; usa borrado criptográfico o destrucción.
- **SPF** = quién puede enviar; **DKIM** = firma; **DMARC** = política + informes.
- **DAC** = decide el propietario; **MAC** = etiquetas; **ABAC** = muchos atributos (incluye contexto).
- Contraseña + PIN = **un factor** (ambos "algo que sabes").
- **SAML** para SSO web empresarial; **OAuth** es autorización, no autenticación; **OIDC** añade autenticación.
- **Falso negativo** es peor que falso positivo.
- **NetFlow** = metadatos; **pcap** = contenido completo.
- **CVE** identifica; **CVSS** puntúa.
- **WPA3** reemplaza PSK por **SAE**.
- Primero capturar **RAM** (más volátil) antes que el disco.
- **Cadena de custodia** rota → evidencia inadmisible.
