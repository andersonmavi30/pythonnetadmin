# Cisco Networking Automation

Python automation examples for Cisco network administration, operations and troubleshooting.

## Implemented frameworks

- **Netmiko** — CLI/SSH operations through `netmiko/operations_toolkit.py`
- **NAPALM** — structured getters and safe configuration preview through `napalm/operations_toolkit.py`
- **Nornir** — inventory-driven multi-device operations through `nornir/operations_toolkit.py`

## Current operational coverage

The current toolkits include examples for:

- Device facts / inventory
- Interface status
- Interface errors
- VLAN information
- ARP table
- MAC address table
- LLDP neighbors
- Routing table
- CPU / memory or environment information
- Running configuration backup
- Troubleshooting command collection
- Multi-device execution with Nornir
- Basic configuration change examples

Configuration changes are protected by an `APPLY_CHANGE = False` variable by default so the examples remain safe for lab validation.

## Structure

```text
Cisco/
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

> Replace the example IP addresses and credentials with lab values before execution. Do not commit production credentials to Git.
