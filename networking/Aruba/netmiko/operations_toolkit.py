#!/usr/bin/env python3
"""
Aruba (Aruba AOS-CX) - Netmiko operations toolkit.

Examples for day-to-day administration, operations and troubleshooting.
Review platform commands against the exact software release used in your lab.
"""

from datetime import datetime
from pathlib import Path

from netmiko import ConnectHandler

DEVICE = {
    "device_type": "aruba_aoscx",
    "host": "192.0.2.10",
    "username": "netadmin",
    "password": "CHANGE_ME",
    "port": 22,
}

OPERATION = "tshoot"
# facts | interfaces | errors | vlans | arp | mac | neighbors | routes | resources | backup | tshoot | all

APPLY_CHANGE = False

COMMANDS = {
    "facts": "show version",
    "interfaces": "show interface brief",
    "errors": "show interface",
    "vlans": "show vlan",
    "arp": "show arp",
    "mac": "show mac-address-table",
    "neighbors": "show lldp neighbor-info detail",
    "routes": "show ip route",
    "resources": "show system resource-utilization"
}
TSHOOT_COMMANDS = [
    "show interface brief",
    "show interface",
    "show ip route",
    "show arp",
    "show mac-address-table",
    "show lldp neighbor-info"
]
BACKUP_COMMAND = "show running-config"
CONFIG_COMMANDS = [
    "interface 1/1/1",
    "description AUTOMATION_TEST"
]

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def save_output(name: str, output: str) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS / f"{DEVICE['host']}_{name}_{stamp}.txt"
    path.write_text(output, encoding="utf-8")
    print(f"[OK] Saved: {path}")


def run_command(connection, name: str, command: str) -> str:
    print(f"\n===== {name.upper()} =====")
    if "\n" in command:
        parts = []
        for item in command.splitlines():
            result = connection.send_command(item, read_timeout=60)
            parts.append(f"===== {item} =====\n{result}")
        output = "\n\n".join(parts)
    else:
        output = connection.send_command(command, read_timeout=60)

    print(output)
    save_output(name, output)
    return output


def main() -> None:
    connection = ConnectHandler(**DEVICE)

    try:
        if OPERATION == "tshoot":
            sections = []
            for command in TSHOOT_COMMANDS:
                result = connection.send_command(command, read_timeout=60)
                section = f"===== {command} =====\n{result}"
                sections.append(section)
                print(section)
            save_output("tshoot", "\n\n".join(sections))

        elif OPERATION == "backup":
            run_command(connection, "backup", BACKUP_COMMAND)

        elif OPERATION == "all":
            for name, command in COMMANDS.items():
                run_command(connection, name, command)

        elif OPERATION in COMMANDS:
            run_command(connection, OPERATION, COMMANDS[OPERATION])

        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")

        if APPLY_CHANGE:
            print("\n[CHANGE] Sending reviewed lab configuration...")
            output = connection.send_config_set(CONFIG_COMMANDS)
            print(output)
            save_output("change", output)
        else:
            print("\n[SAFE] APPLY_CHANGE=False. No configuration changes sent.")

    finally:
        connection.disconnect()


if __name__ == "__main__":
    main()
