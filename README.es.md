# 🐍 Python Network Automation

🇺🇸 [English](README.md)

Repositorio práctico de **Network Automation multi-vendor** enfocado en tareas reales de administración, operación y troubleshooting de redes utilizando Python.

El proyecto está organizado por fabricante/plataforma e implementa progresivamente ejemplos reutilizables con:

- **Netmiko** — automatización SSH/CLI
- **NAPALM** — getters estructurados y flujos de configuración donde exista soporte apropiado
- **Nornir** — orquestación multi-dispositivo basada en inventario
- **pyNTC** — automatización orientada a lifecycle planificada para plataformas soportadas

El repositorio está diseñado alrededor de tareas operativas reales y no solamente de ejemplos aislados de sintaxis.

---

## 🎯 Objetivo del proyecto

El objetivo es construir una caja de herramientas práctica en Python para ingenieros de redes que necesiten:

- Recopilar estado operativo
- Hacer troubleshooting de dispositivos
- Validar la salud de la red
- Realizar backups de configuración
- Ejecutar cambios controlados
- Operar múltiples dispositivos
- Trabajar de forma consistente entre distintos fabricantes

La meta a largo plazo es mantener una misma intención operativa adaptando la implementación a cada fabricante y sistema operativo de red.

---

## 🌐 Cobertura de fabricantes / plataformas

Estado actual:

| Fabricante / Plataforma | Estado | Netmiko | NAPALM | Nornir | pyNTC |
|---|---|---:|---:|---:|---:|
| **Cisco** | ✅ Implementado | ✅ | ✅ | ✅ | Planeado |
| **Arista** | ✅ Implementado | ✅ | ✅ | ✅ | Planeado |
| **Juniper** | ✅ Implementado | ✅ | ✅ | ✅ | Planeado |
| **Aruba AOS-CX** | ✅ Implementado | ✅ | Template con driver externo | ✅ | — |
| **Huawei VRP** | ✅ Implementado | ✅ | Template con driver externo | ✅ | — |
| **Nokia SR OS** | ✅ Implementado | ✅ | Template con driver externo | ✅ | — |
| **SONiC** | ✅ Implementado | Linux SSH / SONiC CLI | Template con driver externo | ✅ | — |
| **Dell OS6 / OS9 / OS10 / Enterprise SONiC** | ✅ Implementado | Multi-perfil | Template con driver externo | ✅ | — |
| **NVIDIA Cumulus Linux / NVUE** | ✅ Implementado | Linux SSH / NVUE | Template con driver externo | ✅ | — |
| **VyOS** | ✅ Implementado | ✅ | Template con driver externo | ✅ | — |

> NAPALM se utilizará únicamente donde exista un driver mantenido y adecuado. No se forzará su uso cuando Netmiko, Nornir, APIs u otro método específico de plataforma sea más apropiado.

---

## 📊 Avance actual

**10 de 10 grupos de fabricantes/plataformas implementados — 100 %**

Tandas completadas:

### Tanda 1
- Cisco
- Arista
- Juniper

Estas plataformas incluyen ejemplos de Netmiko, NAPALM con sus drivers correspondientes y Nornir.

### Tanda 2
- Huawei VRP
- Aruba AOS-CX
- Nokia SR OS

Estas plataformas incluyen toolkits operativos de Netmiko y Nornir, además de un template NAPALM protegido para driver externo. El template NAPALM exige seleccionar y validar explícitamente un driver de terceros antes de ejecutarlo.

### Tanda 3
- Dell OS6 / OS9 / OS10 / Enterprise SONiC
- SONiC
- NVIDIA Cumulus Linux / NVUE
- VyOS

Esta tanda completa la primera base de 10 plataformas. Dell utiliza perfiles separados por sistema operativo, SONiC y NVIDIA siguen un modelo de ejecución orientado a Linux, y VyOS conserva su flujo propio configure/commit/save.

---

## 🗂️ Estructura del repositorio

```text
python_network_automation/
│
├── networking/
│   ├── README.md
│   ├── Cisco/
│   ├── Arista/
│   ├── Juniper/
│   ├── Aruba/
│   ├── Huawei/
│   ├── Nokia/
│   ├── SONiC/
│   ├── Dell/
│   ├── NVIDIA/
│   └── VyOS/
│
├── README.md
├── README.es.md
└── LICENSE
```

Los fabricantes ya implementados siguen actualmente esta estructura:

```text
Vendor/
├── README.md
├── netmiko/
│   └── operations_toolkit.py
├── napalm/
│   └── operations_toolkit.py
└── nornir/
    ├── operations_toolkit.py
    ├── config.yaml
    └── inventory/
        ├── hosts.yaml
        ├── groups.yaml
        └── defaults.yaml
```

---

## 🛠️ Cobertura operativa

Los scripts están enfocados en tareas comunes de administración, operación y troubleshooting como:

- Facts e inventario
- Estado de interfaces
- Errores de interfaces
- Información de VLANs
- Tabla ARP
- Tabla MAC
- Vecinos LLDP
- Tabla de enrutamiento
- CPU / memoria / información de environment
- Backup de running configuration
- Validación de conectividad
- Recolección de comandos de troubleshooting
- Ejecución multi-dispositivo
- Cambios básicos de configuración
- Generación de outputs y artefactos

---

## 🔧 Netmiko

Los ejemplos Netmiko se enfocan en interacción directa por SSH/CLI.

Casos típicos:

- Ejecutar comandos operativos
- Recolectar evidencia para troubleshooting
- Guardar outputs como artefactos
- Realizar backup de configuraciones
- Enviar cambios controlados

Cada fabricante utiliza sus comandos específicos en lugar de asumir que todos los CLI funcionan igual.

---

## 📦 NAPALM

Los ejemplos NAPALM se enfocan en recolección estructurada multi-vendor y flujos seguros de configuración.

Para Cisco, Arista y Juniper el repositorio utiliza directamente los drivers correspondientes de NAPALM. Huawei, Aruba, Nokia, Dell, SONiC, NVIDIA y VyOS utilizan templates protegidos para driver externo con `DRIVER = "CHANGE_ME_DRIVER"`; el repositorio no afirma soporte nativo/core de NAPALM para esas plataformas.

Cuando existe un driver validado, los toolkits pueden exponer getters como:

- Facts
- Interfaces
- Direccionamiento de interfaces
- VLANs
- ARP
- Tabla MAC
- Vecinos LLDP
- Rutas
- Información de environment
- Running configuration

Los ejemplos de configuración utilizan candidate configuration, diff/preview y comportamiento de commit/discard.

---

## 🧵 Nornir

Los ejemplos Nornir proporcionan ejecución multi-dispositivo basada en inventario.

Cada fabricante implementado incluye:

- `config.yaml`
- `hosts.yaml`
- `groups.yaml`
- `defaults.yaml`
- `operations_toolkit.py`

Esto permite ejecutar una misma intención operativa sobre múltiples dispositivos separando credenciales, plataformas y hosts de la lógica Python.

---

## 🔁 Extensión pyNTC planificada

pyNTC está planificado como una cuarta capa complementaria de automatización enfocada en operaciones comunes del ciclo de vida del dispositivo.

Plataformas objetivo iniciales:

- **Cisco**
- **Arista**
- **Juniper**

Casos de uso previstos:

- Facts del dispositivo
- Comandos show
- Obtención de running configuration
- Backups locales
- Save / commit
- Transferencia de archivos y workflows de software donde exista soporte

pyNTC no reemplazará Netmiko, NAPALM ni Nornir. Solo se añadirá donde la librería proporcione soporte apropiado para la plataforma.

---

## 🔒 Cambios seguros por defecto

Los ejemplos que pueden modificar configuración están protegidos mediante:

```python
APPLY_CHANGE = False
```

Por defecto los scripts recopilan información o muestran un preview sin aplicar cambios de configuración.

Para realizar un cambio de laboratorio, el ingeniero debe revisar explícitamente el script y habilitar el comportamiento de cambio.

> Valida siempre los ejemplos primero en laboratorio o entornos controlados antes de adaptarlos a producción.

---

## 🧪 Variables de laboratorio

Los scripts utilizan intencionalmente direccionamiento de documentación/laboratorio como:

```text
192.0.2.10
```

y credenciales placeholder:

```text
username: netadmin
password: CHANGE_ME
```

Reemplaza estos valores con el inventario de tu laboratorio antes de ejecutar.

No almacenes passwords productivos, tokens de API o llaves privadas dentro de Git.

---

## 🧭 Base inicial de fabricantes completada

La primera cobertura multi-vendor ya está completa para los 10 grupos de fabricantes/plataformas definidos.

Las siguientes mejoras pueden incluir:

- TextFSM / parsing estructurado
- Generación de configuración con Jinja2
- Logging y manejo de excepciones
- Reportes CSV / JSON
- Flujos pre-check / post-check
- Validación de configuration diff
- APIs, NETCONF, RESTCONF y gNMI donde aplique
- Tests y validación CI

---

## 📄 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## 👨‍💻 Autor

**Anderson Martinez Virviescas**

Network Administrator | Firewall Administrator | Network Automation | NetDevOps | Linux | Infrastructure Automation

GitHub: [@andersonmavi30](https://github.com/andersonmavi30)

---

> Opera la red. Entiende la plataforma. Automatiza el flujo.
