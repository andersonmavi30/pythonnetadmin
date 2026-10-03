# Aruba Networking Automation

Python automation examples for **Aruba AOS-CX** administration, operations and troubleshooting.

## Implemented frameworks

- **Netmiko** — platform-specific SSH/CLI operations
- **Nornir** — inventory-driven multi-device operations using Netmiko tasks
- **NAPALM template** — prepared for an external maintained driver when one is appropriate for the exact platform/release

## Current operational coverage

The current toolkits include examples for:

- Device facts / version
- Interface status
- Interface counters / error-oriented inspection
- VLAN / service information
- ARP table
- MAC / forwarding table
- LLDP neighbors
- Routing table
- CPU / resource information
- Running configuration backup
- Troubleshooting command collection
- Multi-device execution with Nornir
- Basic configuration change example

Configuration changes remain disabled by default:

```python
APPLY_CHANGE = False
```

## Structure

```text
Aruba/
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

## NAPALM note

The NAPALM example intentionally uses:

```python
DRIVER = "CHANGE_ME_DRIVER"
```

Select, install and validate an appropriate maintained external driver before execution. The repository does not claim native NAPALM support for Aruba AOS-CX.

> Review commands and interface naming against the exact software release used in your lab before enabling configuration changes.
