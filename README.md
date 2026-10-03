# 🐍 Python Network Automation

🇨🇴 [Español](README.es.md)

Practical **multi-vendor Network Automation** repository focused on day-to-day network administration, operations and troubleshooting using Python.

The project is organized by vendor/platform and progressively implements reusable examples with:

- **Netmiko** — SSH/CLI automation
- **NAPALM** — structured getters and configuration workflows where supported
- **Nornir** — inventory-driven multi-device orchestration

The repository is designed around realistic operational tasks rather than isolated syntax examples.

---

## 🎯 Project Objective

The objective is to build a practical Python toolbox for network engineers who need to:

- Collect operational state
- Troubleshoot devices
- Validate network health
- Back up configurations
- Perform controlled configuration changes
- Execute tasks across multiple devices
- Work consistently across multiple vendors

The long-term goal is to keep the same operational intent while adapting the implementation to each vendor and network operating system.

---

## 🌐 Vendor / Platform Coverage

Current project structure:

| Vendor / Platform | Status | Netmiko | NAPALM | Nornir |
|---|---|---:|---:|---:|
| **Cisco** | ✅ Implemented | ✅ | ✅ | ✅ |
| **Arista** | ✅ Implemented | ✅ | ✅ | ✅ |
| **Juniper** | ✅ Implemented | ✅ | ✅ | ✅ |
| **Aruba AOS-CX** | ✅ Implemented | ✅ | External-driver template | ✅ |
| **Huawei VRP** | ✅ Implemented | ✅ | External-driver template | ✅ |
| **Nokia SR OS** | ✅ Implemented | ✅ | External-driver template | ✅ |
| SONiC | Planned | Platform dependent | Community/driver dependent | ✅ planned |
| Dell OS6 / OS9 / OS10 / Enterprise SONiC | Planned | ✅ planned | Driver dependent | ✅ planned |
| NVIDIA Cumulus Linux / NVUE | Planned | Linux SSH / platform dependent | Driver dependent | ✅ planned |
| VyOS | Planned | ✅ planned | Driver dependent | ✅ planned |

> NAPALM is only used where an appropriate maintained driver makes sense. The repository will not force NAPALM support where Netmiko, Nornir, APIs or another platform-specific method is more appropriate.

---

## 📊 Current Progress

**6 of 10 vendor/platform groups implemented — 60%**

Completed waves:

### Wave 1
- Cisco
- Arista
- Juniper

These platforms include Netmiko, native/core NAPALM examples and Nornir.

### Wave 2
- Huawei VRP
- Aruba AOS-CX
- Nokia SR OS

These platforms include Netmiko and Nornir operational toolkits plus a guarded NAPALM external-driver template. The NAPALM template requires an explicitly selected and validated third-party driver before execution.

---

## 🗂️ Repository Structure

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

Implemented vendors currently follow this structure:

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

## 🛠️ Operational Coverage

The scripts are focused on common administration, operations and troubleshooting tasks such as:

- Device facts and inventory
- Interface status
- Interface errors
- VLAN information
- ARP table
- MAC address table
- LLDP neighbors
- Routing table
- CPU / memory / environment information
- Running configuration backup
- Connectivity validation
- Troubleshooting command collection
- Multi-device execution
- Basic configuration changes
- Structured output and artifact generation

---

## 🔧 Netmiko

Netmiko examples focus on direct SSH/CLI interaction.

Typical usage includes:

- Running operational show commands
- Collecting troubleshooting evidence
- Saving outputs to artifacts
- Backing up running configurations
- Sending controlled configuration commands

Each vendor uses platform-specific commands instead of pretending all CLIs behave the same way.

---

## 📦 NAPALM

NAPALM examples focus on structured multi-vendor data collection and safe configuration workflows.

For Cisco, Arista and Juniper, the repository uses the corresponding NAPALM drivers directly. For Huawei, Aruba and Nokia, the repository provides an external-driver template with `DRIVER = "CHANGE_ME_DRIVER"` and does not claim native/core NAPALM support.

Where a validated driver is available, the toolkits can expose getters such as:

- Facts
- Interfaces
- Interface IP information
- VLANs
- ARP
- MAC table
- LLDP neighbors
- Routes
- Environment information
- Running configuration

Configuration examples use candidate configuration, diff/preview and commit/discard behavior.

---

## 🧵 Nornir

Nornir examples provide inventory-driven multi-device execution.

Each implemented vendor includes:

- `config.yaml`
- `hosts.yaml`
- `groups.yaml`
- `defaults.yaml`
- `operations_toolkit.py`

This makes it possible to run the same operational intent against multiple devices while keeping credentials, platform definitions and hosts separated from the Python logic.

---

## 🔒 Safe-by-Default Changes

Configuration-changing examples are protected by:

```python
APPLY_CHANGE = False
```

By default, the examples collect or preview information without applying a configuration change.

To perform a lab change, the engineer must explicitly review the script and enable the change behavior.

> Always test against laboratory or controlled infrastructure before adapting examples to production.

---

## 🧪 Example Lab Variables

The scripts intentionally use documentation/lab addressing such as:

```text
192.0.2.10
```

and placeholder credentials such as:

```text
username: netadmin
password: CHANGE_ME
```

Replace these values with your lab inventory before execution.

Do not commit production passwords, API tokens or private keys to Git.

---

## 🧭 Planned Next Waves

### Wave 3

- Dell OS6 / OS9 / OS10 / Enterprise SONiC
- SONiC
- NVIDIA Cumulus Linux / NVUE
- VyOS

Future additions may also include:

- TextFSM / structured parsing
- Jinja2 configuration generation
- Logging and exception handling
- CSV / JSON reporting
- Pre-check / post-check workflows
- Configuration diff validation
- APIs, NETCONF, RESTCONF and gNMI where appropriate
- Tests and CI validation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👨‍💻 Author

**Anderson Martinez Virviescas**

Network Administrator | Firewall Administrator | Network Automation | NetDevOps | Linux | Infrastructure Automation

GitHub: [@andersonmavi30](https://github.com/andersonmavi30)

---

> Operate the network. Understand the platform. Automate the workflow.
