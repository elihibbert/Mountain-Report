


#Function to find highest temperature in forecast
def find_high_temp(data):
    '''
    This function reports the high and low temperatures for the given location for the week.
    Data is pulled from the National Weather Service (NWS) API for the given location.
    Inputs include the NWS data (expected in JSON format).
    Outputs include the high temperature (in fahrenheit) and date for the week along with the low temp and date.
    '''

    #Import libraries
    import re

    #initiate temperatures list
    temperatures = []

    #Find length of forecast
    forecast_length = len(data['properties']['periods'])

    #Iterate to build the temperatures list with date and temp
    for i in range(forecast_length):
        #record date
        temp_date = data['properties']['periods'][i]['startTime']
        #extract only the date from the forecast starting time - use regular expressions
        _ = re.search("-[0-9][0-9]-[0-9][0-9]",temp_date)
        temp_date = _.group(0)
        
        #record temp
        temp = data['properties']['periods'][i]['temperature']

        #append two values to list as a dict before moving to next forecast date
        temperatures.append({"temp_date": temp_date, "temp": temp})
    
    #find the maximum temperature in the forecast
    high = 0 #initiate high variable
    value_length = (len(temperatures)) #length of value list to loop
    for i in range(value_length):
        #Pull one dict at a time.
        values = temperatures[i]
        if values["temp"] > high:
            #save high
            high = values["temp"]
            #save date
            high_date = values["temp_date"]
        else:
            pass

    #find the minimum temperature in the forecast
    low = 100 #initiate low variable
    for i in range(value_length):
        #Pull one dict at a time.
        values = temperatures[i]
        if values["temp"] < low:
            #save low
            low = values["temp"]
            #save date
            low_date = values["temp_date"]
        else:
            pass
    
    #Return values
    return high, high_date, low, low_date