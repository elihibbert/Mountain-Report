# Mountain-Report
This is a project which gives the week's forecast/report for local ski mountains in the Seattle area.

The main function for the project, titled _mountain_forecast.py_ pulls different functionality from different nested functions with the general goal of reporting the current forecast and reports at the local ski resorts surrounding the greater Seattle, Washington area. All data is currently pulled from National Weather Service (NWS) API's. Ski resorts available currently include Snoqualmie Pass, Stevens Pass, Crystal Mountain Resort, and Baker Ski Area.

Nested functionality currently includes:
  - High and low temperatures for the week. This is created from the nested function _find_high_temp_.
  - Forecasted precipitation for the week. Any chance of precipitation above 50% is reported along with a short description. This is created from the nested function       _precipitation_. 
