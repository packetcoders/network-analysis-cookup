import pandas as pd

# Create a sample df with three columns
data = {
    "device": ["rtr003", "rtr004", "rtr001", "rtr002", "rtr005"],
    "network": [
        "10.1.3.0/24",
        "10.1.4.0/24",
        "10.1.1.0/24",
        "10.1.2.0/24",
        "10.1.5.0/24",
    ],
    "interfaces": [100, 100, 100, 200, 300],
    "version": ["12.1", "12.2", "12.3", "12.1", "12.1"],
    "vrf": ["default", "default", "default", "default", "mgmt"],
}

# Create a df from the sample data
df = pd.DataFrame(data)

# Print the df based on the index location
df.iloc[0]

# Group the df by the version column and count the number of rows in each group
df.groupby(["version"]).size()

# Filter the df based on the vrf and version columns
df.query("vrf == 'default'")
df.query("vrf == 'default' & version > '12.1'")

# Output the df to various formats
df.to_excel("examples/output/output.xlsx", index=False)
df.to_markdown("examples/output/output.md", index=False)

