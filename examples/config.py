import os
from pathlib import Path  # noqa

from dotenv import load_dotenv
from nornir import InitNornir

load_dotenv()

from nornir import InitNornir

nr = InitNornir(
    runner={"plugin": "threaded", "options": {"num_workers": 20}},
    inventory={
        "plugin": "NetBoxInventory2",
        "options": {
            # "host_file": f"{Path(__file__).parent}/inventory/hosts.yaml",
            # "group_file": f"{Path(__file__).parent}/inventory/groups.yaml",
            # "defaults_file": f"{Path(__file__).parent}/inventory/defaults.yaml",
            "nb_url": os.getenv("NETBOX_API"),
            "nb_token": os.getenv("NETBOX_TOKEN"),
            "filter_parameters": {"site": "toronto-data-center"},
            "use_platform_slug": True,
        },
    },
)
