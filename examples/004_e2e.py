#!/usr/bin/env python

import os

try:
    import IPython
except ModuleNotFoundError:
    import code

os.environ["PYTHONINSPECT"] = "TRUE"


import sys
from pathlib import Path

import pandas as pd

sys.path.append(f"{Path(__file__).parent.parent}")

from dotenv import load_dotenv
from nornir.core.task import Result
from nornir_napalm.plugins.tasks import napalm_get

from examples.config import nr

# Load the environment variables from the .env file.
load_dotenv()

# Pull the device username/password from the environment variables and assign to the inventory defaults.
nr.inventory.defaults.username = os.getenv("DEVICE_USERNAME")
nr.inventory.defaults.password = os.getenv("DEVICE_PASSWORD")

# Filter the inventory.
# nr = nr.filter(~F(role__eq="spine"))

# Create a simple custom Nornir task.
def nr_task_dataframe_getter(task, getters):
    # Run the getter task.
    result = task.run(task=napalm_get, getters=getters)

    # Convert the result to a Pandas DataFrame.
    df = pd.DataFrame.from_dict(
        result.result["get_interfaces_counters"], orient="index"
    )

    # Move index to a column and rename it.
    df.reset_index(drop=False, inplace=True)
    df.rename(columns={"index": "interface"}, inplace=True)

    # Return the result.
    return Result(result=df, host=task.host)


def dataframe_builder(getter):
    # Run the getter task.
    result = nr.run(task=nr_task_dataframe_getter, getters=[getter])

    # Explicitly close the connections.
    nr.close_connections()

    # Loop over each device in the Nornir result.
    df_all = []

    for device in result:
        # Get the result from the getter task.
        df = result[device][0].result
        # Add the device name to the DataFrame.
        df.insert(0, "device", device)
        # Append the DataFrame to the list.
        df_all.append(df)

    # Concatenate all the DataFrames in the list into a single DataFrame.
    return pd.concat(df_all, ignore_index=True)


# Condition to ensure code below will only be performed when this module is run (i.e not not imported).
if __name__ == "__main__":
    # Print the results from our executed tasks.
    df = dataframe_builder("get_interfaces_counters")

    #df.to_excel("examples/output/e2e_report.xlsx", sheet_name="all", index=False)
    df_errors = df.query("rx_errors > 0 | tx_errors > 0")
    df_errors.to_excel("examples/output/e2e_report.xlsx", sheet_name="errors", index=False)

    # Check if we are in IPython, an interactive Python shell
    if globals().get("IPython"):
        # If so, start an embedded IPython session
        IPython.embed()
    else:
        # Otherwise, start a default interactive Python session
        code.interact(local=dict(globals(), **locals()))
