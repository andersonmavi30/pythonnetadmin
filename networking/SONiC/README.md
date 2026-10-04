# SONiC Networking Automation

Python automation examples for SONiC administration, operations and troubleshooting.

## Implementation approach

SONiC distributions can differ by vendor and release, so this repository uses a **Linux SSH / SONiC CLI** approach instead of pretending every SONiC implementation exposes an identical network-device driver.

Implemented:

- **Netmiko using the Linux driver**
- **Nornir + Netmiko**
- **NAPALM external-driver template**
- Operational SONiC commands
- `config_db.json` backup example
- Safe-by-default CLI change example

Operational areas include interfaces, counters, VLANs, ARP, MAC table, LLDP, routing, resources, backups and troubleshooting collection.

```python
APPLY_CHANGE = False
```

> Review commands against the exact SONiC distribution in use. Vendor-specific SONiC builds may expose different CLI commands, APIs or management frameworks.
