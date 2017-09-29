import os
import pandas as pd

from pathlib import Path


root = Path(__file__).parents[1]


total_emissions = pd.read_csv(
    root / "archive/EDGARv432_FT2016_CO2_total_emissions_1970-2016.csv",
    skiprows=5
)

assert total_emissions.substance.unique() == "CO2"
total_emissions = total_emissions.drop("substance", axis=1)

total_emissions = total_emissions.rename(columns={
    "ISO_CODE": "Code",
    "ISO_NAME": "Name",
    "sector": "Sector"
})

total_emissions = total_emissions.melt(
    id_vars=["Code", "Name", "Sector"],
    var_name="Year",
    value_name="Emissions"
)

non_standard = [i for i in total_emissions.Code.unique() if len(i) > 3]
print("Non standard country codes:")
print(non_standard)

total_emissions.to_csv(
    "data/edgar-co2-emissions.csv",
    encoding="UTF-8",
    index=False
)
