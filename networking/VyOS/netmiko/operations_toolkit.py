#!/usr/bin/env python3
"""
VyOS - Netmiko operations toolkit.
"""

from datetime import datetime
from pathlib import Path
from netmiko import ConnectHandler

DEVICE = {
    "device_type": "vyos",
    "host": "192.0.2.10",
    "username": "netadmin",
    "password": "CHANGE_ME",
    "port": 22,
}

OPERATION = "tshoot"
APPLY_CHANGE = False

COMMANDS = {
    "facts": "show version",
    "interfaces": "show interfaces",
    "errors": "show interfaces ethernet eth0",
    "vlans": "show interfaces vlan",
    "arp": "show arp",
    "mac": "show bridge",
    "neighbors": "show lldp neighbors detail",
    "routes": "show ip route",
    "resources": "show system memory",
}

BACKUP_COMMAND = "show configuration commands"
TSHOOT_COMMANDS = [
    "show interfaces",
    "show interfaces ethernet eth0",
    "show ip route",
    "show arp",
    "show bridge",
    "show lldp neighbors detail",
]
CHANGE_COMMANDS = [
    "set interfaces ethernet eth0 description 'AUTOMATION_TEST'",
]

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def save_output(name: str, output: str) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS / f"{DEVICE['host']}_{name}_{stamp}.txt"
    path.write_text(output, encoding="utf-8")
    print(f"[OK] Saved: {path}")


def main() -> None:
    connection = ConnectHandler(**DEVICE)

    try:
        if OPERATION == "tshoot":
            sections = []
            for command in TSHOOT_COMMANDS:
                result = connection.send_command(command, read_timeout=60)
                sections.append(f"===== {command} =====\n{result}")
            output = "\n\n".join(sections)
            print(output)
            save_output("tshoot", output)

        elif OPERATION == "backup":
            output = connection.send_command(BACKUP_COMMAND, read_timeout=60)
            print(output)
            save_output("backup", output)

        elif OPERATION == "all":
            for name, command in COMMANDS.items():
                output = connection.send_command(command, read_timeout=60)
                print(f"\n===== {name.upper()} =====\n{output}")
                save_output(name, output)

        elif OPERATION in COMMANDS:
            output = connection.send_command(COMMANDS[OPERATION], read_timeout=60)
            print(output)
            save_output(OPERATION, output)

        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")

        if APPLY_CHANGE:
            connection.send_command_timing("configure")
            for command in CHANGE_COMMANDS:
                connection.send_command_timing(command)
            connection.send_command_timing("commit")
            connection.send_command_timing("save")
            connection.send_command_timing("exit")
            print("[OK] VyOS lab change committed and saved.")
        else:
            print("[SAFE] APPLY_CHANGE=False. No configuration changes sent.")

    finally:
        connection.disconnect()


if __name__ == "__main__":
    main()
