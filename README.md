CO₂ emissions time series 1990-2014 per region/country
provided in the Emissions Database for Global Atmospheric Research (EDGAR) by
the Joint Research Centre (JRC)/PBL Netherlands Environmental Assessment Agency.
The original Excel file data is packaged here in CSV file format.

> 2015 update with 2014 emissions of fossil fuel use and industrial processs emissions (cement production, carbonate use of limestone and dolomite, non-energy use of fuels and other combustion)


# Notes

For convenience three-letter country codes were added to the data when available,
the following have none assigned:

Int. Aviation, Int. Shipping, Serbia and Montenegro, Sudan (former), World

Date: 25/11/2015

Unit: kton (Gg) CO2 per year

> Note that these timeseries report country-specific CO2 emission totals of fossil fuel use and industrial processes (cement production, carbonate use of limestone and dolomite, non-energy use of fuels and other combustion). Excluded are: short-cycle biomass burning (such as agricultural waste burning) and large-scale biomass burning (such as forest fires).


# Sources

The EDGARv4.3FT2014 emissions are calculated based on
	the energy balance statistics of IEA (2014) (http://www.oecd-ilibrary.org/energy/co2-emissions-from-fuel-combustion-2014_co2_fuel-2014-en),
	BP (2013-2014) data of the BP Statistical Review of World Energy, June 2015 (http://www.bp.com/en/global/corporate/about-bp/energy-economics/statisticalreview-of-world-energy.html), Chinese coal comsumption data of the China Statistical Abstract, October 2015 (http://data.stats.gov.cn/english/easyquery.htm?cn=C01).


# Preparation

To update or regenerate the CSV file the following steps need to be run with Python3:

Install requirements:

```
pip install -r scripts/requirements.txt
```

Run the script to generate CSV:
```
python scripts/process.py
```


# Citation

EDGARv4.3, European Commission, Joint Research Centre (JRC)/PBL Netherlands Environmental Assessment Agency. Emission Database for Global Atmospheric Research (EDGAR), release version 4.3. http://edgar.jrc.ec.europe.eu, 2015 forthcoming

The EDGARv4.3FT2014 emissions are calculated based on the energy balance statistics of IEA (2014) (http://www.oecd-ilibrary.org/energy/co2-emissions-from-fuel-combustion-2014_co2_fuel-2014-en) and BP (2013-2014) data of the BP Statistical Review of World Energy, June 2015 (http://www.bp.com/en/global/corporate/about-bp/energy-economics/statisticalreview-of-world-energy.html) and recent Chinese coal comsumption data of the China Statistical Abstract, October 2015 ( http://data.stats.gov.cn/english/easyquery.htm?cn=C01).

Olivier, J.G.J., Janssens-Maenhout, G., Muntean, M. Peters, J.H.A.W., Trends in global CO2 emissions - 2015 report, JRC report 98184 / PBL report 1803, November 2015. (http://edgar.jrc.ec.europa.eu/news_docs/jrc-2015-trends-in-global-co2-emissions-2015-report-98184.pdf)


# License

The [Terms of Use](http://edgar.jrc.ec.europa.eu/terms_of_use.php) of the
Joint Research Centre EDGAR list the following
suggestion for acknowledgment in publications, presentations, websites, etc.:

### Source:

European Commission, Joint Research Centre (JRC)/Netherlands Environmental Assessment Agency (PBL). Emission Database for Global Atmospheric Research (EDGAR), release CO2 time series 1970 - 2014, http://edgar.jrc.ec.europa.e/overview.php?v=CO2ts1990-2014, 2015.

### Reference:

Olivier, J.G.J., Janssens-Maenhout, G., Muntean, M. and Peters, J.A.H.W. (2015) Trends in global CO2 emissions: 2015 Report. PBL Netherlands Environmental Assessment Agency, The Hague; European Commission, Joint Research Centre (JRC), Institute for Environment and Sustainability (IES).  http://edgar.jrc.ec.europa.eu/news_docs/jrc-2015-trends-in-global-co2-emissions-2015-report-98184.pdf. JRC report 98184/ PBL report 1803, 2015.
