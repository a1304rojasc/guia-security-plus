# Dominio 3 · Arquitectura de seguridad (18 %)

> Objetivos oficiales SY0-701: 3.1 – 3.4. Unas 16 preguntas del examen real.

---

## 3.1 Implicaciones de seguridad de distintos modelos de arquitectura

### Nube: modelo de responsabilidad compartida (shared responsibility)

| Capa | On-premises | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Datos y accesos | Cliente | Cliente | Cliente | Cliente |
| Aplicación | Cliente | Cliente | Cliente | Proveedor |
| SO / runtime | Cliente | Cliente | Proveedor | Proveedor |
| Virtualización / hardware / físico | Cliente | Proveedor | Proveedor | Proveedor |

**Regla:** los **datos** y las **identidades** son siempre responsabilidad del cliente.

### Modelos y conceptos
| Concepto | Nota de seguridad |
|---|---|
| Nube híbrida (hybrid) | Complejidad, integración, datos repartidos |
| Terceros (third-party vendors) | Riesgo de proveedor |
| IaC (Infrastructure as Code) | Configuración repetible y auditable; un error se replica |
| Sin servidor (serverless) | Proveedor gestiona la infraestructura; menos control |
| Microservicios | Superficie de ataque mayor (más APIs), pero fallos aislados |
| Aislamiento físico (air-gapped) | Sin conexión de red; riesgo por medios extraíbles |
| Red lógicamente segmentada | VLAN |
| SDN (Software-Defined Networking) | Plano de control separado del de datos |
| On-premises | Control total, coste y responsabilidad total |
| Centralizado vs descentralizado | Punto único de fallo vs gestión compleja |
| Contenedores (containerization) | Comparten kernel del host → menor aislamiento que VM |
| Virtualización | Riesgo de VM escape |
| IoT | Poca capacidad, parches escasos, credenciales por defecto |
| ICS / SCADA | Sistemas industriales; disponibilidad crítica; legacy |
| RTOS (sistema operativo en tiempo real) | Difícil de parchear |
| Sistemas embebidos (embedded) | Hardware dedicado, actualizaciones difíciles |
| Alta disponibilidad (high availability) | Redundancia, clústeres |

**Consideraciones:** disponibilidad, resiliencia, coste, capacidad de respuesta (responsiveness), escalabilidad, facilidad de despliegue, transferencia de riesgo, facilidad de recuperación, capacidad de parchear, potencia, cómputo.

---

## 3.2 Aplicar principios de seguridad a la infraestructura empresarial (escenarios)

### Consideraciones de infraestructura
- **Ubicación de dispositivos** y **zonas de seguridad** (DMZ/screened subnet, interna, invitados).
- **Superficie de ataque**, **conectividad**.
- **Modo de fallo:** *fail-open* (deja pasar si falla → disponibilidad) vs *fail-closed* (bloquea si falla → seguridad).
- **Dispositivo en línea (inline)** vs **pasivo (tap/monitor)**: un IPS va inline; un IDS suele ser pasivo.

### Atributos y dispositivos de red
| Dispositivo | Función |
|---|---|
| Jump server (bastion host) | Servidor intermedio endurecido para administrar zonas seguras |
| Proxy | Intermediario; filtra/oculta clientes (forward) o servidores (reverse) |
| IPS / IDS | Previene (inline) / detecta intrusiones |
| Balanceador de carga (load balancer) | Reparte tráfico; activo-activo / activo-pasivo |
| Sensores | Recogen datos de tráfico |
| Puerto seguro: 802.1X / EAP | Autenticación de puerto (NAC) |
| WAF | Firewall de aplicaciones web (capa 7, bloquea SQLi/XSS) |
| UTM | Todo en uno (firewall, AV, filtrado) |
| NGFW | Firewall de nueva generación; conoce aplicaciones |
| Firewall capa 4 vs capa 7 | Puertos/IPs vs contenido de aplicación |

### Comunicación segura
VPN, acceso remoto, túneles (TLS, IPsec), **SD-WAN**, **SASE** (Secure Access Service Edge: red + seguridad entregadas desde la nube).

### Selección de controles efectivos
Escoger según el riesgo y el escenario (p. ej. WAF para proteger una aplicación web pública).

---

## 3.3 Conceptos y estrategias para proteger datos

### Tipos y clasificación
- **Tipos:** regulados, secretos comerciales, propiedad intelectual, información legal, financiera, legible por humanos / no legible.
- **Clasificación:** sensible, confidencial, pública, restringida, privada, crítica.

### Estados de los datos
| Estado | Protección |
|---|---|
| En reposo (at rest) | Cifrado de disco/BD |
| En tránsito (in transit) | TLS, VPN, IPsec |
| En uso (in use) | Enclaves seguros, cifrado homomórfico, control de memoria |

### Soberanía y geolocalización
- **Soberanía de datos (data sovereignty):** los datos están sujetos a las leyes del país donde se almacenan.
- **Geolocalización:** restringir acceso por ubicación.

### Métodos para proteger datos
| Método | Ejemplo |
|---|---|
| Restricciones geográficas | Bloquear accesos desde fuera de la UE |
| Cifrado | AES-256 |
| Hashing | Verificar integridad |
| Enmascaramiento (masking) | `****-****-****-1234` |
| Tokenización | Sustituir el número de tarjeta por un token |
| Ofuscación | Hacer ilegible el código/datos |
| Segmentación | Separar los datos sensibles |
| Restricción de permisos | ACL, mínimo privilegio |

---

## 3.4 Resiliencia y recuperación en la arquitectura de seguridad

### Alta disponibilidad
Balanceo de carga vs **clústeres (clustering)**. Balanceo reparte tráfico; un clúster ofrece conmutación por error (failover) entre nodos.

### Sitios de recuperación
| Sitio | Preparación | Tiempo de recuperación | Coste |
|---|---|---|---|
| Caliente (hot site) | Equipado y con datos actualizados | Minutos–horas | Alto |
| Templado (warm site) | Hardware, datos parciales | Horas–días | Medio |
| Frío (cold site) | Solo espacio y energía | Días–semanas | Bajo |
| Geográficamente disperso | Evita desastres regionales | — | — |

**Diversidad de plataformas** y **multinube (multi-cloud)** para evitar dependencia de un proveedor.
**Continuidad de operaciones (COOP)** y **planificación de capacidad** (personas, tecnología, infraestructura).

### Pruebas
| Prueba | Descripción |
|---|---|
| Ejercicio de mesa (tabletop) | Discusión del escenario, sin tocar sistemas |
| Conmutación (failover) | Cambiar realmente al sistema secundario |
| Simulación | Escenario simulado más realista |
| Procesamiento paralelo (parallel processing) | Primario y secundario funcionan a la vez para comparar |

### Copias de seguridad (backups)
| Tipo | Copia | Restaurar | Bit de archivo |
|---|---|---|---|
| Completa (full) | Todo | Solo la completa | Se borra |
| Incremental | Cambios desde la **última copia (de cualquier tipo)** | Completa + **todas** las incrementales | Se borra |
| Diferencial | Cambios desde la **última completa** | Completa + **última** diferencial | No se borra |
| Snapshot | Estado en un instante (VM, almacenamiento) | Rápido | — |

Además: on-site/off-site, frecuencia, cifrado, **replicación**, **registro en diario (journaling)**.

### RAID

| Nivel | Técnica | Tolera fallo de | Discos mínimos | Nota |
|---|---|---|---|---|
| RAID 0 | Striping (bandas) | **Ninguno** | 2 | Solo rendimiento, sin redundancia |
| RAID 1 | Espejo (mirroring) | 1 disco | 2 | 50 % de capacidad útil |
| RAID 5 | Bandas con paridad distribuida | 1 disco | 3 | Buen equilibrio |
| RAID 6 | Doble paridad | 2 discos | 4 | Más seguro que RAID 5 |
| RAID 10 (1+0) | Espejo + bandas | 1 por espejo | 4 | Rápido y redundante, caro |

### Energía
| Elemento | Uso |
|---|---|
| SAI (UPS) | Energía **inmediata y corta** (minutos) |
| Generador | Energía **prolongada** (arranca en segundos/minutos) |
| PDU | Distribución de energía en el rack |

---

## Trampas típicas del examen
- En **SaaS** el cliente sigue siendo responsable de los **datos y accesos**.
- **RAID 0 no es redundancia.** RAID no sustituye a las copias de seguridad.
- **Incremental** = backup más rápido, restauración más lenta; **diferencial** = al revés.
- **UPS** para cortes breves; **generador** para cortes largos. Normalmente ambos: el UPS cubre hasta que arranca el generador.
- **Hot site** si piden recuperación en minutos; **cold site** si piden lo más barato.
- **Tabletop** no toca sistemas; **failover** sí.
- **Fail-closed** prioriza seguridad; **fail-open** prioriza disponibilidad.
- **Contenedores** comparten el kernel del host: menos aislamiento que una VM.
- **Soberanía de datos** = leyes del país de almacenamiento.
- **WAF** protege aplicaciones web (SQLi, XSS); un firewall de capa 4 no ve el contenido.
- **Jump server** para administrar zonas protegidas; **proxy inverso** para proteger servidores web.
