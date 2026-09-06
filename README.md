# Python for Network Administrators

Python projects, scripts and labs focused on **Network Automation, Network Programmability, DevNet and NetDevOps**.

This repository documents my progression using Python to automate common network administration tasks and interact programmatically with network infrastructure.

## 🎯 Project Objective

The goal of this repository is to develop practical Python skills applied specifically to networking.

The projects progressively explore how Python can be used to:

- Reduce repetitive network administration tasks
- Configure multiple network devices
- Collect operational information
- Generate configurations
- Validate network state
- Process structured network data
- Interact with devices through SSH and APIs
- Build reusable Network Automation tools

## 🐍 Technology Focus

The repository will progressively cover technologies and libraries such as:

- Python
- Netmiko
- Paramiko
- Jinja2
- REST APIs
- JSON
- YAML
- SSH
- Network device APIs
- Git
- Network Automation
- NetDevOps
- Cisco DevNet concepts

## 🌐 Network Automation Areas

Projects and labs may include:

- Device connectivity
- Configuration deployment
- Multi-device automation
- VLAN automation
- Interface configuration
- Configuration backups
- Configuration validation
- Operational commands
- Inventory processing
- Configuration generation with Jinja2
- Data parsing
- Network health checks
- Pre-check and post-check validation
- API interaction
- Reporting
- Error handling
- Logging

## 📂 Current Labs

### `python_devnet.py`

Early Network Automation lab using Python to connect to multiple **Cisco IOS switches** and automate configuration tasks.

The script demonstrates concepts such as:

- Device connectivity
- Credential input with `getpass`
- Automated CLI configuration
- Hostname configuration
- VLAN creation
- Access port configuration
- Local user configuration
- Console configuration
- Saving device configuration
- Repetitive configuration across multiple switches

### `python_loops_devnet`

Learning exercise focused on introducing Python loops and reducing repetitive network configuration logic.

These scripts represent early stages of the repository and are maintained as part of the learning progression toward more modern Network Automation approaches.

## ⚠️ Legacy Lab Notice

Some initial examples in this repository use **Telnet** and lab credentials for educational purposes.

Telnet does not provide encrypted communication and should not be used for production network administration.

Modern automation developed in this repository will prioritize technologies such as:

- SSH
- Netmiko
- Paramiko
- REST APIs
- NETCONF
- RESTCONF

## ⚙️ Network Automation Evolution

The repository represents a progression from traditional CLI scripting toward more structured Network Automation workflows.

```text
Python Basics
     │
     ▼
CLI Automation
     │
     ▼
SSH / Netmiko
     │
     ▼
Templates / Structured Data
     │
     ▼
APIs / Programmability
     │
     ▼
Network Automation
     │
     ▼
NetDevOps
```

## 📂 Future Repository Structure

As new projects are added, the repository may evolve toward a structure similar to:

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

## 🧪 Lab Environment

The examples in this repository are intended primarily for laboratory and controlled environments.

Always validate scripts and configuration changes before using them against production infrastructure.

## 📊 Repository Status

> 🚧 **Continuous Development**

This repository is part of my continuous development in:

**Python | Network Automation | NetDevOps | DevNet | Network Programmability**

New scripts, labs and automation approaches will be added progressively.

## 👨‍💻 Author

**Anderson Martinez Virviescas**

Network Administrator | Network Automation | NetDevOps | DevNet | Linux | Cybersecurity

GitHub: [@andersonmavi30](https://github.com/andersonmavi30)

---

> See it. Learn it. Code it. Automate it.
