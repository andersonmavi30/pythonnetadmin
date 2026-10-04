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
| Aruba AOS-CX | ✅ Implemented | External-driver template | ✅ Implemented |
| Huawei VRP | ✅ Implemented | External-driver template | ✅ Implemented |
| Nokia SR OS | ✅ Implemented | External-driver template | ✅ Implemented |
| SONiC | ✅ Implemented | External-driver template | ✅ Implemented |
| Dell OS6 / OS9 / OS10 / Enterprise SONiC | ✅ Implemented | External-driver template | ✅ Implemented |
| NVIDIA Cumulus Linux / NVUE | ✅ Implemented | External-driver template | ✅ Implemented |
| VyOS | ✅ Implemented | External-driver template | ✅ Implemented |

> Current progress: **10/10 vendor/platform groups implemented (100%)**. Cisco, Arista and Juniper use their NAPALM drivers directly. Huawei, Aruba, Nokia, Dell, SONiC, NVIDIA and VyOS use guarded external-driver templates where appropriate. Platform-specific execution models are preserved instead of forcing one abstraction across every NOS.
