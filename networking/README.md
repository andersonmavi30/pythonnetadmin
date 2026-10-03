# Networking Automation

This directory contains practical Python examples for day-to-day **network administration, operations and troubleshooting** across multiple vendors and network operating systems.

The labs will be organized by vendor/platform and progressively implemented with:

- **Netmiko** — SSH/CLI automation
- **NAPALM** — structured multi-vendor getters and configuration workflows where supported
- **Nornir** — inventory-driven orchestration for multiple devices

## Vendor Structure

```text
networking/
├── Cisco/
├── Arista/
├── Juniper/
├── Aruba/
├── Huawei/
├── Nokia/
├── SONiC/
├── Dell/
├── NVIDIA/
└── VyOS/
```

## Automation Focus

Examples will cover common operational tasks such as:

- Device facts and inventory
- Interface status and errors
- VLAN information
- Routing table checks
- ARP and MAC table inspection
- Neighbor discovery
- CPU and memory checks
- Configuration backups
- Configuration changes
- Connectivity validation
- Troubleshooting command collection
- Multi-device execution
- Structured reporting

## Framework Coverage

| Vendor / Platform | Netmiko | NAPALM | Nornir |
|---|---:|---:|---:|
| Cisco | ✅ | ✅ | ✅ |
| Arista | ✅ | ✅ | ✅ |
| Juniper | ✅ | ✅ | ✅ |
| Aruba | ✅ | Limited / driver dependent | ✅ |
| Huawei | ✅ | Limited / driver dependent | ✅ |
| Nokia | ✅ / platform dependent | Limited / driver dependent | ✅ |
| SONiC | ✅ / platform dependent | Limited / community driver | ✅ |
| Dell | ✅ | Limited / driver dependent | ✅ |
| NVIDIA Cumulus Linux | ✅ / Linux SSH | Limited / driver dependent | ✅ |
| VyOS | ✅ | Limited / driver dependent | ✅ |

> NAPALM examples will only be added where the selected platform/driver is appropriate and maintainable. Where a native NAPALM driver is not practical, the repository will favor Netmiko, Nornir or platform APIs instead.
