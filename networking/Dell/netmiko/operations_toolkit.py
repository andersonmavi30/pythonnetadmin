#!/usr/bin/env python3
"""
Dell Networking - Netmiko operations toolkit.

Profiles:
- OS6 (legacy)
- OS9 (legacy)
- OS10
- Enterprise SONiC
"""

from datetime import datetime
from pathlib import Path
from netmiko import ConnectHandler

PROFILE = "os10"
OPERATION = "tshoot"
APPLY_CHANGE = False

DEVICE = {
    "host": "192.0.2.10",
    "username": "netadmin",
    "password": "CHANGE_ME",
    "port": 22,
}

PROFILES = {
    "os6": {
        "device_type": "dell_powerconnect",
        "commands": {
            "facts": "show version",
            "interfaces": "show interfaces status",
            "errors": "show interfaces counters errors",
            "vlans": "show vlan",
            "arp": "show arp",
            "mac": "show mac address-table",
            "neighbors": "show lldp neighbors detail",
            "routes": "show ip route",
            "resources": "show process cpu",
        },
        "backup": "show running-config",
        "tshoot": [
            "show interfaces status",
            "show interfaces counters errors",
            "show ip route",
            "show arp",
            "show mac address-table",
            "show lldp neighbors detail",
        ],
        "config": ["interface gigabitethernet 1/0/1", "description AUTOMATION_TEST"],
        "shell_change": False,
    },
    "os9": {
        "device_type": "dell_force10",
        "commands": {
            "facts": "show version",
            "interfaces": "show interfaces status",
            "errors": "show interfaces counters errors",
            "vlans": "show vlan",
            "arp": "show arp",
            "mac": "show mac-address-table",
            "neighbors": "show lldp neighbors detail",
            "routes": "show ip route",
            "resources": "show processes cpu",
        },
        "backup": "show running-config",
        "tshoot": [
            "show interfaces status",
            "show interfaces counters errors",
            "show ip route",
            "show arp",
            "show mac-address-table",
            "show lldp neighbors detail",
        ],
        "config": ["interface TenGigabitEthernet 0/1", "description AUTOMATION_TEST"],
        "shell_change": False,
    },
    "os10": {
        "device_type": "dell_os10",
        "commands": {
            "facts": "show version",
            "interfaces": "show interface status",
            "errors": "show interface counters errors",
            "vlans": "show vlan",
            "arp": "show ip arp",
            "mac": "show mac address-table",
            "neighbors": "show lldp neighbors detail",
            "routes": "show ip route",
            "resources": "show processes cpu",
        },
        "backup": "show running-configuration",
        "tshoot": [
            "show interface status",
            "show interface counters errors",
            "show ip route",
            "show ip arp",
            "show mac address-table",
            "show lldp neighbors detail",
        ],
        "config": ["interface ethernet 1/1/1", "description AUTOMATION_TEST"],
        "shell_change": False,
    },
    "enterprise_sonic": {
        "device_type": "linux",
        "commands": {
            "facts": "show version",
            "interfaces": "show interfaces status",
            "errors": "show interfaces counters errors",
            "vlans": "show vlan brief",
            "arp": "show arp",
            "mac": "show mac",
            "neighbors": "show lldp table",
            "routes": "show ip route",
            "resources": "top -bn1 | head -20",
        },
        "backup": "cat /etc/sonic/config_db.json",
        "tshoot": [
            "show interfaces status",
            "show interfaces counters errors",
            "show ip route",
            "show arp",
            "show mac",
            "show lldp table",
        ],
        "config": [
            "sudo config interface description Ethernet0 AUTOMATION_TEST",
            "sudo config save -y",
        ],
        "shell_change": True,
    },
}

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def save_output(name: str, output: str) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS / f"{DEVICE['host']}_{PROFILE}_{name}_{stamp}.txt"
    path.write_text(output, encoding="utf-8")
    print(f"[OK] Saved: {path}")


def main() -> None:
    profile = PROFILES[PROFILE]
    device = {**DEVICE, "device_type": profile["device_type"]}
    connection = ConnectHandler(**device)

    try:
        if OPERATION == "tshoot":
            sections = []
            for command in profile["tshoot"]:
                result = connection.send_command(command, read_timeout=60)
                sections.append(f"===== {command} =====\n{result}")
            output = "\n\n".join(sections)
            print(output)
            save_output("tshoot", output)

        elif OPERATION == "backup":
            output = connection.send_command(profile["backup"], read_timeout=60)
            print(output)
            save_output("backup", output)

        elif OPERATION == "all":
            for name, command in profile["commands"].items():
                output = connection.send_command(command, read_timeout=60)
                print(f"\n===== {name.upper()} =====\n{output}")
                save_output(name, output)

        elif OPERATION in profile["commands"]:
            output = connection.send_command(profile["commands"][OPERATION], read_timeout=60)
            print(output)
            save_output(OPERATION, output)

        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")

        if APPLY_CHANGE:
            if profile["shell_change"]:
                for command in profile["config"]:
                    print(connection.send_command_timing(command))
            else:
                print(connection.send_config_set(profile["config"]))
        else:
            print("[SAFE] APPLY_CHANGE=False. No configuration changes sent.")

    finally:
        connection.disconnect()


if __name__ == "__main__":
    main()
