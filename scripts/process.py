import os
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
co2_emissions_excel = os.path.join(
    path, "../archive/CO2_1970-2014_dataset_of_CO2_report_2015.xls")
co2_emissions_csv = os.path.join(path, "../data/edgar-co2-emissions.csv")

df = pd.read_excel(
    co2_emissions_excel,
    skiprows=12
)

df = df.dropna()

url = ("https://raw.githubusercontent.com/" +
       "datasets/country-codes/master/data/country-codes.csv")

country_codes = pd.read_csv(
    url,
    index_col="official_name_en",
    usecols=["ISO3166-1-Alpha-3", "official_name_en"],
    encoding="UTF-8"
)
country_codes = country_codes.rename(
    columns={"ISO3166-1-Alpha-3": "Code"}
)


# Add country codes for spelling variations and EU28.
additions = {
    "China, Hong Kong SAR": "HKG",
    "China, Macao SAR": "MAC",
    "China, Taiwan Province of": "TWN",
    "Côte d Ivoire": "CIV",
    "Democratic People s Republic of Korea": "PRK",
    "Faroe Islands": "FRO",
    "Lao People s Democratic Republic": "LAO",
    "Netherlands Antilles": "ANT",
    "United Kingdom": "GBR",
    "EU28": "EU28"
}

# Without country code:
#  "Serbia and Montenegro"
#  "Sudan (former)"
#  "Int. Aviation"
#  "Int. Shipping"
#  "World"

additions = pd.DataFrame({"Code": list(additions.values())},
                         index=additions.keys())
country_codes = country_codes.append(additions)

df = df.set_index("Country")

df = df.join(country_codes)

print("Without country code:")
print(", ".join(df.loc[df["Code"].isnull()].index.values))

df.index.name = "Name"

output = pd.melt(
    df.reset_index(),
    id_vars=["Name", "Code"],
    var_name="Year",
    value_name="Emissions"
)

output = output.sort_values(["Name", "Year"])

output.to_csv(
    co2_emissions_csv,
    encoding="UTF-8",
    index=False
)
