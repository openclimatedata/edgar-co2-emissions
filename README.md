Data Package of the EDGAR’s Global Fossil CO2 Emissions from 1970 to 2017 (EDGARv5.0_FT2017 dataset)

Timeseries 1970–2017 of CO₂ emissions by country and sector (Buildings, Power Industry, Transport, Other industrial combustion, Other sectors) in Mt CO₂/year.

Source: European Commission, Joint Research Centre (EC-JRC)/Netherlands Environmental Assessment Agency (PBL). Emissions Database for Global Atmospheric Research (EDGAR), release EDGARv5.0_FT2017  (1970–2017), http://edgar.jrc.ec.europa.eu/overview.php?v=booklet2018, 2018-11-23.

For more information or data JRC-EDGAR@ec.europa.eu

# Notes

Unit: Mt CO₂ per year

Non-standard country codes:

FRA_MCO, ISR_PSE, ITA_SMR_VAT, SRB_MNE, ESP_AND, SDN_SSD, CHE_LIE, AIR, SEA

(WORLD and EU28 were removed in EDGARv5.0)

> In this report fossil CO2 emissions include sources from fossil fuel use (combustion, flaring), industrial processes (cement, steel, chemicals and urea) and product use. Please note that in the analysis presented in this report no short cycle carbon CO2 is included in any sector.
>
> EDGARv5.0 uses international activity data, mainly energy balance statistics of IEA (2017) for 1970-2015 to estimate CO2 from fossil fuel consumption. These emissions are extended (FT approach) to 2016 and 2017 using BP statistics. The respective sectoral breakdowns of emissions for 2015 are extrapolated to 2016 and 2017.
>
> Updates for 2016 and 2017 for cement, lime, ammonia and ferroalloys production are based on USGS statistics, urea production and consumption are based on IFA
> statistics, associated gas used from flaring from GGFR/NOAA, steel production from world steel and cement clinker production from UNFCCC (2018b).
>
> For the other sectors with lower contributions to the global CO2 emissions, the time series in EDGARv4.3.2 have been extended for the period 2013-2017 using proxy data and relative changes in activity data compared to 2012, reported in recent data sources.


# References

BP 2015-2017 data of the BP Statistical Review of World Energy, (June 2018) (https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html).

IEA energy balance statistics for 1970-2015 (2017) (http://www.iea.org/).

Olivier, J.G.J. and J.A.H.W. Peters (2018), Trend in Global CO2 and GHG Emissions - 2018 Report, PBL Report no.3125.

IFA 2011-2016 urea consumption and production statistics (June 2018) (http://www.fertilizer.org/Statistics).

USGS (2018), 2010-2017 data of cement, lime, ammonia and ferroalloys of the USGS Commodity Statistics (May 2018) (https://minerals.usgs.gov/minerals/pubs/commodity/).

WB (2018) for data of GDP (expressed in 1000 US dollar, and adjusted to the Purchasing Power Parity of 2011) for 1990-2017 (World Bank, July 2018).

World Steel Association (worldsteel, November 2017). Steel Statistical Yearbook 2017 (https://www.worldsteel.org/en/dam/jcr:3e275c73-6f11-4e7f-a5d8-23d9bc5c508f/Steel%2520Statistical%2520Yearbook%25202017_updated%2520version090518.pdf).

IMF/WEO data of annual GDP growth (2018) for missing data in the WB dataset for recent years. World Economic Outlook Update April 2018. International Monetary Fund.

UNDP population statistics (2017), World Population Prospects (WPP), The 2017 Revision Report United Nations, Department of Economic and Social Affairs, Population Division.


# Preparation

The `Makefile` requires Python3 and will automatically install its dependencies
into a Virtualenv when run with

```shell
make
```


# Citation

Muntean, M., Guizzardi, D., Schaaf, E., Crippa, M., Solazzo, E., Olivier, J.G.J., Vignati, E. Fossil CO2 emissions of all world countries - 2018 Report, EUR 29433 EN, Publications Office of the European Union, Luxembourg, 2018, ISBN 978-92-79-97240-9, doi:10.2760/30158, JRC113738.


# License

See also [Terms of Use](http://edgar.jrc.ec.europa.eu/terms_of_use.php).
