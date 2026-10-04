# NVIDIA Networking Automation

Python automation examples focused on **NVIDIA Cumulus Linux and NVUE**.

## Implementation approach

Cumulus Linux is Linux-based, so the automation examples combine Linux networking commands with **NVUE** where appropriate.

Implemented:

- **Netmiko using Linux SSH**
- **Nornir + Netmiko**
- **NAPALM external-driver template**
- NVUE system/interface/bridge examples
- Linux ARP, FDB and route inspection
- `nv config show` backup example
- Safe-by-default NVUE change example

Operational areas include interfaces, bridge domains, ARP, FDB/MAC, LLDP, routes, resources, backups and troubleshooting.

```python
APPLY_CHANGE = False
```

> Validate NVUE syntax against the Cumulus Linux release used in your lab before enabling configuration changes.
