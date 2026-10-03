#!/usr/bin/env python3
"""
Arista - Netmiko operations toolkit
Day-to-day administration, operations and troubleshooting examples.
"""

from datetime import datetime
from pathlib import Path
from netmiko import ConnectHandler

# ===== LAB VARIABLES =====
DEVICE = {
    "device_type": "arista_eos",
    "host": "192.0.2.10",
    "username": "netadmin",
    "password": "CHANGE_ME",
    "port": 22,
}

OPERATION = "tshoot"
# facts | interfaces | errors | vlans | arp | mac | neighbors | routes | resources | backup | tshoot | all

APPLY_CHANGE = False
INTERFACE_CHANGE = ["interface Ethernet1","description AUTOMATION_TEST"]

COMMANDS = {
    "facts": "show version",
    "interfaces": "show ip interface brief",
    "errors": "show interfaces counters errors",
    "vlans": "show vlan",
    "arp": "show arp",
    "mac": "show mac address-table",
    "neighbors": "show lldp neighbors detail",
    "routes": "show ip route",
    "resources": "show processes top once"
}
TSHOOT_COMMANDS = [
    "show ip interface brief",
    "show interfaces status",
    "show ip route",
    "show arp",
    "show mac address-table",
    "show lldp neighbors detail"
]
BACKUP_COMMAND = "show running-config"

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def save_output(name: str, output: str) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS / f"{DEVICE['host']}_{name}_{stamp}.txt"
    path.write_text(output, encoding="utf-8")
    print(f"[OK] Saved: {path}")


def run_show(connection, name: str, command: str) -> None:
    print(f"\n===== {name.upper()} =====")
    output = connection.send_command(command, read_timeout=60)
    print(output)
    save_output(name, output)


def main() -> None:
    connection = ConnectHandler(**DEVICE)
    try:
        if OPERATION == "tshoot":
            output = []
            for command in TSHOOT_COMMANDS:
                result = connection.send_command(command, read_timeout=60)
                output.append(f"\n===== {command} =====\n{result}")
                print(output[-1])
            save_output("tshoot", "\n".join(output))

        elif OPERATION == "backup":
            run_show(connection, "backup", BACKUP_COMMAND)

        elif OPERATION == "all":
            for name, command in COMMANDS.items():
                run_show(connection, name, command)

        elif OPERATION in COMMANDS:
            run_show(connection, OPERATION, COMMANDS[OPERATION])

        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")

        if APPLY_CHANGE:
            print("\n[CHANGE] Sending basic lab change...")
            output = connection.send_config_set(INTERFACE_CHANGE)
            print(output)
            save_output("change", output)
        else:
            print("\n[SAFE] APPLY_CHANGE=False. No configuration change sent.")

    finally:
        connection.disconnect()


if __name__ == "__main__":
    main()
