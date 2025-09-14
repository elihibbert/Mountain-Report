#Function under the mountain forecast file which records the precipitation forecasted.


#Import libraries
import re



#This function will check for precipitation and report it
def precipitation(data):
    
    #Find length of forecast
    forecast_length = len(data['properties']['periods'])

    #What is the threshold of precipitation to report?
    threshold = 50 #<-----------------------minimum percent of precip to report-----------------------

    #Initiate precip report list
    precipitation_report = []

    #Loop through forecast, save date, description and precip chance if above threshold. 
    for i in range(forecast_length):
        #Temporarily save values each loop
        values = data['properties']['periods'][i]
        probability = values['probabilityOfPrecipitation']['value']
        #If probability > threshold
        if probability >= threshold:
            #Save date and description
            probability_date = values['startTime']
            #extract only the date from the forecast starting time - use regular expressions
            _ = re.search("-[0-9][0-9]-[0-9][0-9]", probability_date)
            probability_date = _.group(0)
            probability_description = values['detailedForecast']

            #Append to precipition report
            precipitation_report.append({"probability": probability, "date": probability_date, "description": probability_description})

        else:
            pass
    


    #Return precip report
    return threshold, precipitation_report