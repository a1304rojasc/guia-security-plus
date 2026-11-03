# Dominio 2 · Amenazas, vulnerabilidades y mitigaciones (22 %)

> Objetivos oficiales SY0-701: 2.1 – 2.5. Unas 19–20 preguntas del examen real.

---

## 2.1 Actores de amenaza (threat actors) y motivaciones

| Actor | Recursos / sofisticación | Motivación típica | Ejemplo |
|---|---|---|---|
| Estado-nación (nation-state) | Muy altos; APT (Advanced Persistent Threat) | Espionaje, guerra, disrupción | Grupo patrocinado que roba propiedad intelectual durante meses |
| Crimen organizado (organized crime) | Altos | Económica | Ransomware como servicio |
| Hacktivista (hacktivist) | Medios | Ideológica / filosófica | DDoS contra una empresa por motivos medioambientales |
| Interno (insider threat) | Acceso legítimo | Venganza, dinero | Empleado despedido que borra datos |
| Aficionado (unskilled attacker / script kiddie) | Bajos; herramientas ajenas | Notoriedad, diversión | Lanza un escáner descargado |
| TI en la sombra (shadow IT) | Bajos | Comodidad (no maliciosa) | Departamento que usa un SaaS no aprobado |

**Atributos:** interno/externo, recursos/financiación, nivel de sofisticación.
**Motivaciones (lista oficial):** exfiltración de datos, espionaje, interrupción del servicio, chantaje, financiera, filosófica/política, venganza, disrupción/caos, guerra.

---

## 2.2 Vectores de amenaza (threat vectors) y superficies de ataque

- **Basados en mensajes:** correo, SMS, mensajería instantánea.
- **Basados en imágenes**, **basados en archivos**, **llamadas de voz**.
- **Medios extraíbles** (USB abandonado en el parking).
- **Software vulnerable:** cliente con agente vs sin agente (agentless).
- **Software sin soporte** (end-of-life).
- **Redes inseguras:** inalámbricas, cableadas, Bluetooth.
- **Puertos abiertos y servicios**, **credenciales por defecto** (admin/admin).
- **Cadena de suministro (supply chain):** proveedores de servicios gestionados (MSP), vendedores, proveedores.

### Ingeniería social (human vectors)
| Técnica | Descripción |
|---|---|
| Phishing | Correo fraudulento masivo |
| Spear phishing / whaling | Dirigido a una persona / a un directivo |
| Vishing | Por voz (llamada) |
| Smishing | Por SMS |
| Desinformación / información errónea (misinformation/disinformation) | Información falsa (intencional o no) |
| Suplantación (impersonation) | Hacerse pasar por otra persona (técnico, jefe) |
| Compromiso de correo empresarial (BEC) | Cuenta legítima comprometida pide transferencias |
| Pretexto (pretexting) | Historia inventada para justificar la petición |
| Abrevadero (watering hole) | Infectar un sitio que la víctima visita |
| Suplantación de marca (brand impersonation) | Web/correo que imita una marca |
| Typosquatting | Dominio con error tipográfico: `g00gle.com` |

---

## 2.3 Tipos de vulnerabilidades

| Categoría | Ejemplos |
|---|---|
| Aplicación | Inyección en memoria (memory injection), desbordamiento de búfer (buffer overflow), condición de carrera (race condition: **TOCTOU**, time-of-check to time-of-use), actualización maliciosa (malicious update) |
| Sistema operativo | Falta de parches, escalada de privilegios |
| Web | Inyección SQL (SQLi), cross-site scripting (XSS) |
| Hardware | Firmware vulnerable, fin de vida (end-of-life), heredado (legacy) |
| Virtualización | Escape de máquina virtual (VM escape), reutilización de recursos (resource reuse) |
| Nube | Configuración errónea (p. ej. bucket público) |
| Cadena de suministro | Proveedor de servicios, hardware o software comprometido |
| Criptográfica | Algoritmos débiles, claves cortas |
| Configuración errónea (misconfiguration) | Puertos abiertos, permisos excesivos |
| Móvil | Carga lateral (side loading), jailbreak/root |
| Día cero (zero-day) | Vulnerabilidad sin parche conocido |

---

## 2.4 Analizar indicadores de actividad maliciosa (escenarios)

### Malware

| Tipo | Rasgo clave | Indicador |
|---|---|---|
| Ransomware | Cifra datos y pide rescate | Archivos con extensión nueva, nota de rescate |
| Troyano (trojan) | Se disfraza de software legítimo | Programa "gratis" con comportamiento extraño |
| RAT | Troyano de acceso remoto | Conexiones salientes persistentes |
| Gusano (worm) | Se **autopropaga** por la red sin intervención | Pico de tráfico, muchos hosts infectados |
| Virus | Necesita que el usuario lo ejecute; se adjunta a archivos | Archivos modificados |
| Spyware | Espía la actividad | Datos enviados a terceros |
| Bloatware | Software preinstalado innecesario | Consumo de recursos |
| Keylogger | Registra pulsaciones | Robo de credenciales |
| Bomba lógica (logic bomb) | Se activa ante una condición (fecha, evento) | Borrado al eliminar a un usuario de nómina |
| Rootkit | Se oculta a nivel de kernel/sistema | Procesos invisibles para el SO |
| Sin archivos (fileless) | Vive en memoria, usa PowerShell/WMI | Sin archivos en disco |

### Ataques físicos
Fuerza bruta física, clonación RFID (RFID cloning), ambientales (cortar energía/climatización).

### Ataques de red
| Ataque | Descripción |
|---|---|
| DDoS amplificado / reflejado (amplified / reflected) | Respuestas grandes (DNS, NTP) dirigidas a la víctima |
| Ataques DNS | Envenenamiento de caché, secuestro de dominio |
| Inalámbricos | Punto de acceso falso (rogue AP / evil twin), desautenticación |
| En ruta (on-path, antes MITM) | El atacante intercepta el tráfico |
| Repetición de credenciales (credential replay) | Reutilizar un hash/token capturado (pass-the-hash) |
| Malware de red | Gusanos, botnets |

### Ataques a aplicaciones
Inyección (SQL, comandos), desbordamiento de búfer, repetición (replay), escalada de privilegios, falsificación de petición (CSRF/forgery), recorrido de directorios (directory traversal: `../../etc/passwd`).

### Ataques criptográficos
Degradación (downgrade: forzar TLS antiguo), colisión (collision: dos entradas, mismo hash), cumpleaños (birthday attack).

### Ataques a contraseñas
| Ataque | Descripción |
|---|---|
| Rociado (password spraying) | **Pocas** contraseñas comunes contra **muchas** cuentas (evita bloqueos) |
| Fuerza bruta (brute force) | Todas las combinaciones contra una cuenta |
| Diccionario | Lista de palabras |

### Indicadores (IoC)
Bloqueo de cuentas, viaje imposible (impossible travel: login desde Madrid y Tokio en 10 min), acceso concurrente a sesiones, recurso bloqueado, consumo de recursos fuera de lo normal, contenido publicado/filtrado, registros desaparecidos (missing logs), eventos fuera de ciclo (out-of-cycle logging).

---

## 2.5 Técnicas de mitigación para proteger la empresa

| Técnica | Qué hace |
|---|---|
| Segmentación (segmentation) | Separar redes (VLAN, subredes) para limitar el movimiento lateral |
| Control de acceso | ACL, permisos |
| Lista de aplicaciones permitidas (application allow list) | Solo se ejecuta software aprobado |
| Aislamiento (isolation) | Separar un sistema comprometido |
| Parcheo (patching) | Corregir vulnerabilidades |
| Cifrado | Proteger datos |
| Monitorización | Detectar anomalías |
| Mínimo privilegio (least privilege) | Solo los permisos necesarios |
| Configuración segura | Baselines |
| Desmantelamiento (decommissioning) | Retirar activos de forma segura |

**Técnicas de bastionado (hardening):** cifrado, instalar EDR, firewall basado en host, HIPS, deshabilitar puertos/protocolos, cambiar contraseñas por defecto, eliminar software innecesario.

---

## Trampas típicas del examen
- **Gusano** se propaga solo; **virus** necesita acción del usuario.
- **Bomba lógica** = condición; si el escenario menciona "cuando el empleado fue eliminado de RR. HH." → bomba lógica.
- **Password spraying** vs **brute force**: si hay *muchas cuentas* con *pocas contraseñas* y no hay bloqueos → spraying.
- **Hacktivista** = ideología; **crimen organizado** = dinero; **estado-nación** = APT, persistencia, espionaje.
- **Shadow IT** es una amenaza interna **no intencionada**.
- **Whaling** apunta a altos directivos; **BEC** usa una cuenta legítima comprometida.
- **Typosquatting** (dominio mal escrito) ≠ **watering hole** (infectar un sitio legítimo frecuentado).
- **TOCTOU** es una **condición de carrera**.
- **Viaje imposible** es un indicador de cuenta comprometida.
- Mitigar un sistema legacy sin parches → **segmentación/aislamiento** (control compensatorio).
- **Directory traversal** se reconoce por `../`; **XSS** por `<script>`; **SQLi** por `' OR 1=1 --`.
