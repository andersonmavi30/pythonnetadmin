#!/usr/bin/env python3
"""
Huawei (Huawei VRP) - Nornir operations toolkit.

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
    "facts": "display version",
    "interfaces": "display ip interface brief",
    "errors": "display interface",
    "vlans": "display vlan",
    "arp": "display arp",
    "mac": "display mac-address",
    "neighbors": "display lldp neighbor verbose",
    "routes": "display ip routing-table",
    "resources": "display cpu-usage\ndisplay memory-usage"
}
TSHOOT_COMMANDS = [
    "display ip interface brief",
    "display interface",
    "display ip routing-table",
    "display arp",
    "display mac-address",
    "display lldp neighbor"
]
BACKUP_COMMAND = "display current-configuration"
CONFIG_COMMANDS = [
    "interface GigabitEthernet0/0/1",
    "description AUTOMATION_TEST"
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
