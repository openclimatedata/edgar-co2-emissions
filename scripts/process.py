import pandas as pd

from pathlib import Path
from countrynames import to_code_3

root = Path(__file__).parents[1]

extra_codes = {
    "North Macedonia": "MKD",
    "France and Monaco": "FRA_MCO",
    "Israel and Palestine, State of": "ISR_PSE",
    "Italy, San Marino and the Holy See": "ITA_SMR_VAT",
    "Spain and Andorra": "ESP_AND",
    "Sudan and South Sudan": "SDN_SSD",
    "Switzerland and Liechtenstein": "CHE_LIE",
    "Faroes": "FRO",
    "International Aviation": "AIR",
    "International Shipping": "SEA",
}


def to_code(name):
    code = to_code_3(name)
    if code is None:
        try:
            code = extra_codes[name]
        except KeyError:
            code = None
    return code


co2_emissions = pd.read_excel(
    root / "archive/EDGARv5.0_FT2018_fossil_CO2_GHG_booklet2019.xls",
    sheet_name="fossil_CO2_by_sector_and_countr",
)

co2_emissions["Code"] = co2_emissions.country_name.apply(to_code)
co2_emissions = co2_emissions.rename(columns={"country_name": "Name"})

years = range(1970, 2019)
co2_emissions = co2_emissions.melt(
    id_vars=["Code", "Name", "Sector"],
    value_vars=years,
    var_name="Year",
    value_name="Emissions",
)

co2_emissions = co2_emissions.set_index(["Code", "Name", "Sector"])

co2_emissions.to_csv("data/edgar-co2-emissions.csv", encoding="UTF-8")
