#!/usr/bin/env python3
"""
NVIDIA Cumulus Linux / NVUE - Netmiko/Linux operations toolkit.
"""

from datetime import datetime
from pathlib import Path
from netmiko import ConnectHandler

DEVICE = {
    "device_type": "linux",
    "host": "192.0.2.10",
    "username": "netadmin",
    "password": "CHANGE_ME",
    "port": 22,
}

OPERATION = "tshoot"
APPLY_CHANGE = False

COMMANDS = {
    "facts": "nv show system",
    "interfaces": "nv show interface",
    "errors": "ip -s link",
    "vlans": "nv show bridge domain",
    "arp": "ip neigh show",
    "mac": "bridge fdb show",
    "neighbors": "lldpctl",
    "routes": "ip route show",
    "resources": "top -bn1 | head -20"
}
BACKUP_COMMAND = "nv config show"
CHANGE_COMMANDS = [
    "sudo nv set interface swp1 description AUTOMATION_TEST",
    "sudo nv config apply"
]
TSHOOT_COMMANDS = [
    COMMANDS["interfaces"],
    COMMANDS["errors"],
    COMMANDS["arp"],
    COMMANDS["mac"],
    COMMANDS["neighbors"],
    COMMANDS["routes"],
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
            for command in CHANGE_COMMANDS:
                print(connection.send_command_timing(command))
        else:
            print("[SAFE] APPLY_CHANGE=False. No configuration changes sent.")

    finally:
        connection.disconnect()


if __name__ == "__main__":
    main()
