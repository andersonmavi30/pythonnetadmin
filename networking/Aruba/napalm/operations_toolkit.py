#!/usr/bin/env python3
"""
Aruba (Aruba AOS-CX) - NAPALM external-driver template.

NAPALM does not provide the same native/core driver coverage for every
platform in this repository. Install and validate an appropriate maintained
driver before using this example.
"""

import json
from datetime import datetime
from pathlib import Path

from napalm import get_network_driver

DRIVER = "CHANGE_ME_DRIVER"
HOST = "192.0.2.10"
USERNAME = "netadmin"
PASSWORD = "CHANGE_ME"

OPERATION = "all"
ROUTE_LOOKUP = "0.0.0.0/0"

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def save_json(name: str, data) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS / f"{HOST}_{name}_{stamp}.json"
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    print(f"[OK] Saved: {path}")


def safe_getter(device, name, function) -> None:
    print(f"\n===== {name.upper()} =====")
    try:
        data = function()
        print(json.dumps(data, indent=2, default=str))
        save_json(name, data)
    except Exception as exc:
        print(f"[WARN] {name} unsupported or failed with selected driver: {exc}")


def main() -> None:
    if DRIVER == "CHANGE_ME_DRIVER":
        raise SystemExit(
            "Set DRIVER to an installed and validated external NAPALM driver "
            "for this platform before execution."
        )

    driver = get_network_driver(DRIVER)
    device = driver(HOST, USERNAME, PASSWORD, optional_args={})
    device.open()

    getters = {
        "facts": device.get_facts,
        "interfaces": device.get_interfaces,
        "interfaces_ip": device.get_interfaces_ip,
        "vlans": device.get_vlans,
        "arp": device.get_arp_table,
        "mac": device.get_mac_address_table,
        "neighbors": device.get_lldp_neighbors_detail,
        "routes": lambda: device.get_route_to(destination=ROUTE_LOOKUP),
        "environment": device.get_environment,
        "backup": lambda: device.get_config(retrieve="running"),
    }

    try:
        if OPERATION == "all":
            for name, function in getters.items():
                safe_getter(device, name, function)
        elif OPERATION in getters:
            safe_getter(device, OPERATION, getters[OPERATION])
        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")
    finally:
        device.close()


if __name__ == "__main__":
    main()
