from pathlib import Path

from nornir import InitNornir

nr = InitNornir(
    runner={"plugin": "threaded", "options": {"num_workers": 20}},
    inventory={
        "plugin": "SimpleInventory",
        "options": {
            "host_file": f"{Path(__file__).parent}/inventory/hosts.yaml",
            "group_file": f"{Path(__file__).parent}/inventory/groups.yaml",
            #"defaults_file": f"{Path(__file__).parent}/inventory/defaults.yaml",
        },
    },
)
