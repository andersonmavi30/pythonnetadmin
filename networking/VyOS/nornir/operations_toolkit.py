#!/usr/bin/env python3
"""
VyOS - Nornir operations toolkit.
"""

from datetime import datetime
from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

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
    "configure",
    "set interfaces ethernet eth0 description 'AUTOMATION_TEST'",
    "commit",
    "save",
    "exit",
]

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def collect(task: Task) -> Result:
    if OPERATION == "tshoot":
        commands = TSHOOT_COMMANDS
    elif OPERATION == "backup":
        commands = [BACKUP_COMMAND]
    else:
        commands = [COMMANDS[OPERATION]]

    sections = []
    for command in commands:
        result = task.run(
            task=netmiko_send_command,
            command_string=command,
            read_timeout=60,
        )
        sections.append(f"===== {command} =====\n{result.result}")

    if APPLY_CHANGE:
        for command in CHANGE_COMMANDS:
            task.run(
                task=netmiko_send_command,
                command_string=command,
                use_timing=True,
            )

    return Result(host=task.host, result="\n\n".join(sections))


def save_results(result) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for host, multi_result in result.items():
        path = ARTIFACTS / f"{host}_{OPERATION}_{stamp}.txt"
        path.write_text(str(multi_result[-1].result), encoding="utf-8")
        print(f"[OK] Saved: {path}")


def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=collect)
    print_result(result)
    save_results(result)

    if not APPLY_CHANGE:
        print("[SAFE] APPLY_CHANGE=False. No configuration changes sent.")


if __name__ == "__main__":
    main()
