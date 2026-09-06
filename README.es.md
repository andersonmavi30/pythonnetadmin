# Python para Administradores de Redes

🇺🇸 [English](README.md)

Proyectos, scripts y laboratorios en Python enfocados en **Network Automation, Network Programmability, DevNet y NetDevOps**.

Este repositorio documenta mi evolución utilizando Python para automatizar tareas comunes de administración de redes e interactuar programáticamente con infraestructura de red.

## 🎯 Objetivo del Proyecto

El objetivo de este repositorio es desarrollar habilidades prácticas de Python aplicadas específicamente a networking.

Los proyectos exploran progresivamente cómo Python puede utilizarse para:

- Reducir tareas repetitivas de administración de red
- Configurar múltiples dispositivos de red
- Recopilar información operativa
- Generar configuraciones
- Validar el estado de la red
- Procesar datos estructurados de red
- Interactuar con dispositivos mediante SSH y APIs
- Construir herramientas reutilizables de Network Automation

## 🐍 Enfoque Tecnológico

El repositorio cubrirá progresivamente tecnologías y librerías como:

- Python
- Netmiko
- Paramiko
- Jinja2
- REST APIs
- JSON
- YAML
- SSH
- APIs de dispositivos de red
- Git
- Network Automation
- NetDevOps
- Conceptos de Cisco DevNet

## 🌐 Áreas de Network Automation

Los proyectos y laboratorios pueden incluir:

- Conectividad con dispositivos
- Despliegue de configuraciones
- Automatización multi-dispositivo
- Automatización de VLANs
- Configuración de interfaces
- Backups de configuración
- Validación de configuración
- Comandos operativos
- Procesamiento de inventarios
- Generación de configuraciones con Jinja2
- Parsing de datos
- Health checks de red
- Validaciones pre-check y post-check
- Interacción con APIs
- Reportes
- Manejo de errores
- Logging

## 📂 Laboratorios Actuales

### `python_devnet.py`

Laboratorio inicial de Network Automation utilizando Python para conectarse a múltiples **switches Cisco IOS** y automatizar tareas de configuración.

El script demuestra conceptos como:

- Conectividad con dispositivos
- Ingreso de credenciales con `getpass`
- Configuración automatizada por CLI
- Configuración de hostname
- Creación de VLANs
- Configuración de puertos de acceso
- Configuración de usuarios locales
- Configuración de consola
- Guardado de configuración
- Configuración repetitiva sobre múltiples switches

### `python_loops_devnet`

Ejercicio de aprendizaje enfocado en introducir bucles de Python y reducir lógica repetitiva de configuración de red.

Estos scripts representan etapas iniciales del repositorio y se mantienen como parte de la evolución hacia enfoques más modernos de Network Automation.

## ⚠️ Aviso sobre Laboratorios Legacy

Algunos ejemplos iniciales de este repositorio utilizan **Telnet** y credenciales de laboratorio con fines educativos.

Telnet no proporciona comunicación cifrada y no debe utilizarse para administración de redes en producción.

La automatización moderna desarrollada en este repositorio priorizará tecnologías como:

- SSH
- Netmiko
- Paramiko
- REST APIs
- NETCONF
- RESTCONF

## ⚙️ Evolución de Network Automation

El repositorio representa una progresión desde scripting CLI tradicional hacia flujos de Network Automation más estructurados.

```text
Fundamentos de Python
     │
     ▼
Automatización CLI
     │
     ▼
SSH / Netmiko
     │
     ▼
Templates / Datos Estructurados
     │
     ▼
APIs / Programabilidad
     │
     ▼
Network Automation
     │
     ▼
NetDevOps
```

## 📂 Estructura Futura del Repositorio

A medida que se agreguen nuevos proyectos, el repositorio puede evolucionar hacia una estructura similar a:

```text
pythonnetadmin/
│
├── basics/
├── netmiko/
├── paramiko/
├── jinja2/
├── api/
├── parsing/
├── network-tools/
├── labs/
├── docs/
└── README.md
```

## 🧪 Entorno de Laboratorio

Los ejemplos de este repositorio están destinados principalmente a laboratorios y entornos controlados.

Siempre valida los scripts y cambios de configuración antes de utilizarlos sobre infraestructura productiva.

## 📊 Estado del Repositorio

> 🚧 **Desarrollo Continuo**

Este repositorio forma parte de mi desarrollo continuo en:

**Python | Network Automation | NetDevOps | DevNet | Network Programmability**

Se agregarán progresivamente nuevos scripts, laboratorios y enfoques de automatización.

## 👨‍💻 Autor

**Anderson Martinez Virviescas**

Network Administrator | Network Automation | NetDevOps | DevNet | Linux | Cybersecurity

GitHub: [@andersonmavi30](https://github.com/andersonmavi30)

---

> See it. Learn it. Code it. Automate it.
