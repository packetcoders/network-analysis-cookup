# Network Analysis Cookup
This repo contains code and examples from the NetDevOps day talk:
> Cooking Up A Network Analysis Stack with Nornir, NAPALM and Pandas.

## File Layout

`./examples/001_napalm.py` - Basic example of NAPALM and the use of getters.
`./examples/002_nornir.py` - Basic example of using Nornir with NAPALM.
`./examples/003_pandas.py` - Basic examples of using Pandas.
`./examples/004_e2e.py` - An example of using all 3 tools together to collect data from a network and aggregate all the data into a single data frame.

## Setup
If you would like to try these scripts out yourself, please follow the steps below:

```
python -m .venv venv
source .venv/bin/activate

pip install -r requirements.txt
```