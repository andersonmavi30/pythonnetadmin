#!/usr/bin/env python3
"""
Cisco - NAPALM operations toolkit
Structured getters, backup and safe configuration preview.
"""

import json
from datetime import datetime
from pathlib import Path
from napalm import get_network_driver

# ===== LAB VARIABLES =====
DRIVER = "ios"
HOST = "192.0.2.10"
USERNAME = "netadmin"
PASSWORD = "CHANGE_ME"

ROUTE_LOOKUP = "0.0.0.0/0"
OPERATION = "all"
# facts | interfaces | interfaces_ip | vlans | arp | mac | neighbors | routes | environment | backup | all

APPLY_CHANGE = False
CANDIDATE_CONFIG = """interface GigabitEthernet1\n description AUTOMATION_TEST"""

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"


def save_json(name: str, data) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS / f"{HOST}_{name}_{stamp}.json"
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    print(f"[OK] Saved: {path}")


def safe_getter(device, name, function):
    print(f"\n===== {name.upper()} =====")
    try:
        data = function()
        print(json.dumps(data, indent=2, default=str))
        save_json(name, data)
    except Exception as exc:
        print(f"[WARN] {name} not supported or failed: {exc}")


def main() -> None:
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
            for name, fn in getters.items():
                safe_getter(device, name, fn)
        elif OPERATION in getters:
            safe_getter(device, OPERATION, getters[OPERATION])
        else:
            raise ValueError(f"Unsupported OPERATION: {OPERATION}")

        if CANDIDATE_CONFIG.strip():
            print("\n===== CONFIGURATION PREVIEW =====")
            device.load_merge_candidate(config=CANDIDATE_CONFIG)
            diff = device.compare_config()
            print(diff or "[OK] No differences")

            if APPLY_CHANGE and diff:
                device.commit_config()
                print("[OK] Configuration committed.")
            else:
                device.discard_config()
                print("[SAFE] Candidate discarded. Set APPLY_CHANGE=True to commit.")

    finally:
        device.close()


if __name__ == "__main__":
    main()
