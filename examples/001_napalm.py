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

# Pull the device username/password from the environment variables and assign to the inventory defaults.
username = os.getenv("DEVICE_USERNAME")
password = os.getenv("DEVICE_PASSWORD")

# Initialize the NAPALM driver for EOS.
eos_driver = get_network_driver("eos")

# fmt: off
# Create a context manager to open the connection to the device and close the connection when complete.
with eos_driver(hostname="172.29.151.7", username=username, password=password) as device:
    # View the other gettters
    rprint(f"{device.get_facts()}")

    # Get the interfaces counters
    rprint("="*80)
    rprint(device.get_interfaces_counters())

    # Get the BGP neighbors
    rprint("="*80)
    rprint(device.get_bgp_neighbors())

    # Get the device version and platform
    rprint("="*80)
    rprint(device.get_facts())

    # Get the CPU and memory utilization
    rprint("="*80)
    rprint(device.get_environment())
# fmt: on