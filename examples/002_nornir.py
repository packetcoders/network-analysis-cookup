#!/usr/bin/env python

import os
import sys
from pathlib import Path


sys.path.append(f"{Path(__file__).parent.parent}")

from dotenv import load_dotenv
from nornir.core.filter import F
from nornir.core.task import Result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result

from examples.config import nr

# Load the environment variables from the .env file.
load_dotenv()

# Pull the device username/password from the environment variables and assign to the inventory defaults.
nr.inventory.defaults.username = os.getenv("DEVICE_USERNAME")
nr.inventory.defaults.password = os.getenv("DEVICE_PASSWORD")

# Filter the inventory.
#nr = nr.filter(~F(role__eq="spine"))

GETTERS = ["get_interfaces_counters", "get_bgp_neighbors", "get_facts", "get_environment"]
OUTPUT = Path(__file__).parent / "output"

# Create a simple custom Nornir task.
def task_napalm_getter_to_file(task, output ,getters):
    # Run the getter task.
    getter_results = task.run(task=napalm_get, getters=getters)

    # Write the result to a file.
    write_result = write_file(
        task=task,
        filename=f"{output}/{task.host.name}.json",
        content=str(getter_results.result)
        )

    # Return the result.
    return Result(result=write_result, host=task.host)

# Run our Nornir task.
result = nr.run(task=task_napalm_getter_to_file, output=OUTPUT,getters=GETTERS)

# Explicitly close the connections.
nr.close_connections()

# Condition to ensure code below will only be performed when this module is run (i.e not not imported).
if __name__ == "__main__":
    # Print the results from our executed tasks.
    print_result(result, vars=["stdout"])
    #nornir_inspect(result)
