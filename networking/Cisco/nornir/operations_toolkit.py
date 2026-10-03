#!/usr/bin/env python3
"""
Cisco - Nornir operations toolkit
Inventory-driven multi-device operations using Netmiko tasks.
"""

from datetime import datetime
from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

# ===== OPERATION VARIABLES =====
OPERATION = "tshoot"
# facts | interfaces | errors | vlans | arp | mac | neighbors | routes | resources | backup | tshoot

APPLY_CHANGE = False
CONFIG_COMMANDS = ["interface GigabitEthernet1","description AUTOMATION_TEST"]

COMMANDS = {
    "facts": "show version",
    "interfaces": "show ip interface brief",
    "errors": "show interfaces counters errors",
    "vlans": "show vlan brief",
    "arp": "show ip arp",
    "mac": "show mac address-table",
    "neighbors": "show lldp neighbors detail",
    "routes": "show ip route",
    "resources": "show processes cpu | include CPU|show processes memory | include Processor"
}
TSHOOT_COMMANDS = [
    "show ip interface brief",
    "show interfaces status",
    "show ip route",
    "show ip arp",
    "show mac address-table",
    "show lldp neighbors detail"
]
BACKUP_COMMAND = "show running-config"

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def collect(task: Task) -> Result:
    commands = TSHOOT_COMMANDS if OPERATION == "tshoot" else [
        BACKUP_COMMAND if OPERATION == "backup" else COMMANDS[OPERATION]
    ]

    sections = []
    for command in commands:
        result = task.run(
            task=netmiko_send_command,
            command_string=command,
            read_timeout=60,
        )
        sections.append(f"===== {command} =====\n{result.result}")

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
