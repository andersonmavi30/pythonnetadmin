#!/usr/bin/env python3
"""
Nokia (Nokia SR OS) - Nornir operations toolkit.

Inventory-driven multi-device operations using Nornir + Netmiko.
"""

from datetime import datetime
from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

OPERATION = "tshoot"
# facts | interfaces | errors | vlans | arp | mac | neighbors | routes | resources | backup | tshoot

APPLY_CHANGE = False

COMMANDS = {
    "facts": "show version",
    "interfaces": "show port",
    "errors": "show port statistics",
    "vlans": "show service",
    "arp": "show router arp",
    "mac": "show service fdb-mac",
    "neighbors": "show system lldp neighbor",
    "routes": "show router route-table",
    "resources": "show system cpu"
}
TSHOOT_COMMANDS = [
    "show port",
    "show port statistics",
    "show router route-table",
    "show router arp",
    "show service fdb-mac",
    "show system lldp neighbor"
]
BACKUP_COMMAND = "admin display-config"
CONFIG_COMMANDS = [
    "port 1/1/1",
    "description \"AUTOMATION_TEST\""
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
        command_list = command.splitlines()
        for command_item in command_list:
            result = task.run(
                task=netmiko_send_command,
                command_string=command_item,
                read_timeout=60,
            )
            sections.append(f"===== {command_item} =====\n{result.result}")

    if APPLY_CHANGE:
        task.run(
            task=netmiko_send_config,
            config_commands=CONFIG_COMMANDS,
        )

    return Result(host=task.host, result="\n\n".join(sections))


def save_results(result) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for host, multi_result in result.items():
        final = multi_result[-1].result
        path = ARTIFACTS / f"{host}_{OPERATION}_{stamp}.txt"
        path.write_text(str(final), encoding="utf-8")
        print(f"[OK] Saved: {path}")


def main() -> None:
    if OPERATION not in COMMANDS and OPERATION not in {"backup", "tshoot"}:
        raise ValueError(f"Unsupported OPERATION: {OPERATION}")

    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=collect)

    print_result(result)
    save_results(result)

    if not APPLY_CHANGE:
        print("[SAFE] APPLY_CHANGE=False. No configuration changes sent.")


if __name__ == "__main__":
    main()
