#!/usr/bin/env python3
"""
SONiC - Nornir/Linux operations toolkit.
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
    "interfaces": "show interfaces status",
    "errors": "show interfaces counters errors",
    "vlans": "show vlan brief",
    "arp": "show arp",
    "mac": "show mac",
    "neighbors": "show lldp table",
    "routes": "show ip route",
    "resources": "top -bn1 | head -20"
}
BACKUP_COMMAND = "cat /etc/sonic/config_db.json"
CHANGE_COMMANDS = [
    "sudo config interface description Ethernet0 AUTOMATION_TEST",
    "sudo config save -y"
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
