#!/usr/bin/env python3
"""
Cisco - pyNTC operations toolkit.

Profiles:
- IOS / IOS-XE
- NX-OS
- IOS-XR

Safe-by-default examples for facts, show commands, running configuration,
local backups, save/commit and controlled configuration changes.
"""

import json
from datetime import datetime
from pathlib import Path

from pyntc import ntc_device as NTC

PROFILE = "ios"
# ios | nxos | iosxr

HOST = "192.0.2.10"
USERNAME = "netadmin"
PASSWORD = "CHANGE_ME"

OPERATION = "facts"
# facts | show | running_config | backup | save | config

ALLOW_SAVE = False
ALLOW_CONFIG_CHANGE = False

PROFILES = {
    "ios": {
        "device_type": "cisco_ios_ssh",
        "connection": {"port": 22},
        "show_commands": [
            "show version",
            "show ip interface brief",
            "show ip route",
        ],
        "config_commands": [
            "interface Loopback999",
            "description PYNTC_LAB",
        ],
        "supports_save": True,
    },
    "nxos": {
        "device_type": "cisco_nxos_nxapi",
        "connection": {"transport": "https", "port": 443},
        "show_commands": [
            "show version",
            "show interface brief",
            "show ip route",
        ],
        "config_commands": [
            "interface loopback999",
            "description PYNTC_LAB",
        ],
        "supports_save": True,
    },
    "iosxr": {
        "device_type": "cisco_iosxr_ssh",
        "connection": {"port": 22},
        "show_commands": [
            "show version",
            "show interfaces brief",
            "show route",
        ],
        "config_commands": [
            "interface Loopback999",
            "description PYNTC_LAB",
        ],
        "supports_save": False,
    },
}

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def build_device():
    profile = PROFILES[PROFILE]
    params = {
        "host": HOST,
        "username": USERNAME,
        "password": PASSWORD,
        "device_type": profile["device_type"],
    }
    params.update(profile["connection"])
    return NTC(**params)


def backup_path() -> Path:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return ARTIFACTS / f"{HOST}_{PROFILE}_{stamp}.cfg"


def main() -> None:
    if PROFILE not in PROFILES:
        raise SystemExit(f"Unsupported PROFILE: {PROFILE}")

    profile = PROFILES[PROFILE]
    device = build_device()

    try:
        if OPERATION == "facts":
            print(json.dumps(device.facts, indent=2, default=str))

        elif OPERATION == "show":
            print(device.show(profile["show_commands"], raw_text=True))

        elif OPERATION == "running_config":
            print(device.running_config)

        elif OPERATION == "backup":
            path = backup_path()
            device.backup_running_config(str(path))
            print(f"[OK] Backup saved: {path}")

        elif OPERATION == "save":
            if not profile["supports_save"]:
                raise SystemExit(f"save() is not used for profile {PROFILE}.")
            if not ALLOW_SAVE:
                raise SystemExit("Set ALLOW_SAVE=True after reviewing the operation.")
            device.save()
            print("[OK] Configuration saved.")

        elif OPERATION == "config":
            if not ALLOW_CONFIG_CHANGE:
                raise SystemExit(
                    "Set ALLOW_CONFIG_CHANGE=True after reviewing the commands."
                )
            device.config(profile["config_commands"])
            print("[OK] Configuration commands sent.")

        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")

    finally:
        device.close()


if __name__ == "__main__":
    main()
