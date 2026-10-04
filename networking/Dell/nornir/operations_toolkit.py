#!/usr/bin/env python3
"""
Dell Networking - Nornir multi-generation operations toolkit.

Inventory includes OS6, OS9, OS10 and Enterprise SONiC examples.
"""

from datetime import datetime
from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

OPERATION = "tshoot"
APPLY_CHANGE = False

PROFILES = {
    "os6": {
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
        "tshoot": ["show interfaces status", "show interfaces counters errors", "show ip route", "show arp"],
        "config": ["interface gigabitethernet 1/0/1", "description AUTOMATION_TEST"],
        "shell_change": False,
    },
    "os9": {
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
        "tshoot": ["show interfaces status", "show interfaces counters errors", "show ip route", "show arp"],
        "config": ["interface TenGigabitEthernet 0/1", "description AUTOMATION_TEST"],
        "shell_change": False,
    },
    "os10": {
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
        "tshoot": ["show interface status", "show interface counters errors", "show ip route", "show ip arp"],
        "config": ["interface ethernet 1/1/1", "description AUTOMATION_TEST"],
        "shell_change": False,
    },
    "enterprise_sonic": {
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
        "tshoot": ["show interfaces status", "show interfaces counters errors", "show ip route", "show arp"],
        "config": ["sudo config interface description Ethernet0 AUTOMATION_TEST", "sudo config save -y"],
        "shell_change": True,
    },
}

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def collect(task: Task) -> Result:
    profile_name = task.host.data.get("profile", "os10")
    profile = PROFILES[profile_name]

    if OPERATION == "tshoot":
        commands = profile["tshoot"]
    elif OPERATION == "backup":
        commands = [profile["backup"]]
    else:
        commands = [profile["commands"][OPERATION]]

    sections = []
    for command in commands:
        result = task.run(
            task=netmiko_send_command,
            command_string=command,
            read_timeout=60,
        )
        sections.append(f"===== {command} =====\n{result.result}")

    if APPLY_CHANGE:
        if profile["shell_change"]:
            for command in profile["config"]:
                task.run(task=netmiko_send_command, command_string=command, use_timing=True)
        else:
            task.run(task=netmiko_send_config, config_commands=profile["config"])

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
