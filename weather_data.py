#Function under the mountain forecast file which pulls national weather service data for the given location.




#Import Libraries
import requests
import sys 



#Function to import raw data for the forecast from national weather service. 
#Input resorts variable which defines what weather report to use.
def weather_data(resorts):

    #All the possible resorts hardcoded into the program
    resort_locations = [{"resort": "snoqualmie pass", "resort lat": "47.4266", "resort lon": "-121.4154"},
                        {"resort": "stevens pass", "resort lat": "47.7462", "resort lon": "-121.0859"},
                        {"resort": "crystal resort", "resort lat": "46.9291", "resort lon": "-121.5009"},
                        {"resort": "mt baker", "resort lat": "48.777", "resort lon": "-121.814"}]

    #Loop through the resort_locations to find the location the user requests
    resort_locations_length = len(resort_locations)
    for i in range(resort_locations_length):
        if resort_locations[i]["resort"] == resorts:
            lat = resort_locations[i]["resort lat"]
            lon = resort_locations[i]["resort lon"]
        else:
            pass

    #Build the initial API using the resorts coordinates
    initial_api = "https://api.weather.gov/points/" + lat + "," + lon 

    #Go to the first NWS API to obtain the second API. Use try statement to avoid weird errors
    try:
        initial_data = requests.get(initial_api)
    except requests.RequestException:
        sys.exit("An error pulling the initial weather API was found. Please check link.")
    else:
        initial_data = initial_data.json()
        
    #Save the "grid formation" url
    forecast_api = initial_data["properties"]["forecast"]

    #Use the grid formation url to go to the second API and save forecast data
    try:
        data = requests.get(forecast_api)
    except requests.RequestException:
        sys.exit("An error pulling the weather API was found. Please check link.")
    else:
        data = data.json()

    #Return the forecast data
    return data
    


'''
How the National Weather Service API works...
Start with Lat and Lon coordinates (i.e. 47.4231N and 121.3942W)
Go to the first NWS API --> https://api.weather.gov/points/47.4231,-121.3942
On this API, we can pull the forecast API based upon their "grid location"
This url is located under [properties][forecast] and is called --> https://api.weather.gov/gridpoints/PDT/63,197/forecast
Once at this API, all the data needed can be pulled.
'''