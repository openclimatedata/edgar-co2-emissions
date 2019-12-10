Data Package with CSV files of EDGAR’s Global Fossil CO2 Emissions from 1970 to 2018 (EDGARv5.0_FT2018 dataset)

Timeseries 1970–2018 of CO₂ emissions by country and sector (Buildings, Power Industry, Transport, Other industrial combustion, Other sectors) in Mt CO₂/year.

Dataset name: EDGARv5.0_FT2018

Website: https://edgar.jrc.ec.europa.eu/overview.php?v=booklet2019

GHG emissions are not yet included in the Data Package.


# Methods

Unit: Mt CO₂ per year

Non-standard country codes:

FRA_MCO, ISR_PSE, ITA_SMR_VAT, CSXX, ESP_AND, SDN_SSD, CHE_LIE, AIR, SEA

> In this report fossil CO₂ emissions include sources from fossil fuel use (combustion, flaring), industrial processes (cement, steel, chemicals and urea) and product use.
> Please note that in the analysis presented in this report no short cycle carbon CO2 is included in any sector.
> GHG emissions comprise fossil CO2, CH4, N2O and F-gases.
>
> EDGARv5.0 uses international activity data, mainly energy balance statistics of IEA
> (2017) for 1970-2015 to estimate CO₂ from fossil fuel consumption. These emissions
> are extended (FT approach) up to 2018 using BP statistics keeping the same sectoral breakdown.
> Updates for 2016, 2017 and 2018 for cement, lime, ammonia and ferroalloys production are
> based on USGS statistics, urea production and consumption are based on IFA
> statistics, associated gas used from flaring from GGFR/NOAA, steel production from
> world steel and cement clinker production from UNFCCC (2019).
> GHG emissions are estimated entirely using stable statistics and no Fast-Track approach is applied.
> Therefore GHG emissions are available until the year 2015.


# References

BP 2015-2018 data of the BP Statistical Review of World Energy, https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html, June 2019.

IEA energy balance statistics for 1970-2015 (2017) (http://www.iea.org/).

Olivier, J.G.J. and J.A.H.W. Peters (2019), Trend in Global CO2 and GHG Emissions - 2019 Report, PBL Report, 2019.

IFA 2013-2016 urea consumption and production statistics, https://www.fertilizer.org/, June 2019.

IMF/WEO data of annual GDP growth for missing data in the WB dataset for recent years. World Economic Outlook Update April 2019. International Monetary Fund, 2019.

UNDP population statistics (2019), World Population Prospects (WPP), The 2019 Revision Report United Nations, Department of Economic and Social Affairs, Population Division, 2019.

USGS: 2010-2018 data of cement, lime, ammonia and ferroalloys of the USGS Commodity Statistics (June 2019), (https://minerals.usgs.gov/minerals/pubs/commodity/), 2019.

WB data of GDP (expressed in 1000 US dollar, and adjusted to the Purchasing Power Parity of 2011) for 1990-2018, World Bank, July 2019.

World Steel Association, worldsteel, Steel Statistical Yearbook 2018, https://www.worldsteel.org/en/dam/jcr:e5a8eda5-4b46-4892-856b-00908b5ab492/SSY_2018.pdf), November 2018.


# Preparation

The `Makefile` requires Python3 and will automatically install its dependencies
into a Virtualenv when run with

```shell
make
```


# Citation

Crippa, M., Oreggioni, G., Guizzardi, D., Muntean, M., Schaaf, E., Lo Vullo, E., Solazzo, E., Monforti-Ferrario, F., Olivier, J.G.J., Vignati, E., Fossil CO2 and GHG emissions of all world countries - 2019 Report, EUR 29849 EN, Publications Office of the European Union, Luxembourg, 2019, ISBN 978-92-76-11100-9, https://doi.org/10.2760/687800, JRC117610.


# License

See also [Terms of Use](http://edgar.jrc.ec.europa.eu/terms_of_use.php).
