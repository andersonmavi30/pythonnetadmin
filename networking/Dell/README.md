# Dell Networking Automation

Python automation examples for Dell network administration, operations and troubleshooting across multiple generations.

## Implemented platform profiles

- **Dell Networking OS6 (legacy)** — Netmiko profile: `dell_powerconnect`
- **Dell Networking OS9 (legacy)** — Netmiko profile: `dell_force10`
- **Dell SmartFabric OS10** — Netmiko profile: `dell_os10`
- **Dell Enterprise SONiC** — Linux/SONiC-oriented profile

The Netmiko toolkit uses a `PROFILE` variable so OS6, OS9, OS10 and Enterprise SONiC are not treated as if they shared the same CLI.

## Implemented frameworks

- **Netmiko** — multi-generation operational profiles
- **Nornir** — sample inventory containing all four Dell platform families
- **NAPALM template** — external-driver template only; no native/core support is claimed

## Operational coverage

- Version / facts
- Interfaces and counters
- VLANs
- ARP
- MAC table
- LLDP
- Routing table
- CPU/resources
- Configuration backup
- Troubleshooting collection
- Basic safe-by-default changes

```python
APPLY_CHANGE = False
```

## Structure

```text
Dell/
├── README.md
├── netmiko/operations_toolkit.py
├── napalm/operations_toolkit.py
└── nornir/
    ├── operations_toolkit.py
    ├── config.yaml
    └── inventory/
        ├── hosts.yaml
        ├── groups.yaml
        └── defaults.yaml
```

> Validate exact CLI syntax against the Dell software release and hardware platform used in your lab before enabling changes.
