#!/usr/bin/env python

import os
import sys
from pathlib import Path

sys.path.append(f"{Path(__file__).parent.parent.parent.parent}")

from dotenv import load_dotenv
from napalm import get_network_driver
from rich import print as rprint

# Load the environment variables from the .env file.
load_dotenv()


# Initialize the NAPALM driver for napalm.
napalm_driver = get_network_driver("eos")

device = {
    "hostname": "leaf5.lab.packetcoders.io",
    "username": os.getenv("DEVICE_USERNAME"),
    "password": os.getenv("DEVICE_PASSWORD"),
}

# fmt: off
# Create a context manager to open the connection to the device and close the connection when complete.
with napalm_driver(**device) as napalm_conn:
    # Get the interfaces counters
    rprint("="*80)
    rprint(napalm_conn.get_interfaces_counters())

    # Get the BGP neighbors
    rprint("="*80)
    rprint(napalm_conn.get_bgp_neighbors())

    # Get the device version and platform
    rprint("="*80)
    rprint(napalm_conn.get_facts())

    # Get the CPU and memory utilization
    rprint("="*80)
    rprint(napalm_conn.get_environment())
# fmt: on
