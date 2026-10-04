# VyOS Networking Automation

Python automation examples for VyOS administration, operations and troubleshooting.

## Implemented frameworks

- **Netmiko** — VyOS operational CLI and controlled configuration workflow
- **Nornir + Netmiko** — inventory-driven multi-device operations
- **NAPALM external-driver template** — requires an appropriate maintained external driver

## Operational coverage

- Version / facts
- Interfaces
- Interface detail / error-oriented inspection
- VLAN interfaces
- ARP
- Bridge information
- LLDP neighbors
- IPv4 routing table
- System resources
- Configuration backup with `show configuration commands`
- Troubleshooting collection
- Basic configuration workflow using `configure → set → commit → save`

Changes are disabled by default:

```python
APPLY_CHANGE = False
```

> Validate commands against the VyOS release used in your lab before enabling changes.
