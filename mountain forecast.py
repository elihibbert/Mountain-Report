#This is a file which will pull weather forecasts/reports for local ski mountains. Various functions are nested beneath the main function.




def main():
    '''
    This is a function which generates weather forecasts and reports for local Washington ski resorts.
    Based upon user input of resort, nested functions are called to get various forecast/report functionality.
    Current funcationality includes; high and low temperatures for the week, and any precipiation forecasted for the week.
    Data is pulled from the National Weather Service API's.
    Inputs are not needed
    No outputs are used however this function will print results.    
    '''

    #Import functions from other files
    import sys
    from weather_data import weather_data
    from find_high_temp import find_high_temp
    from precipitation import precipitation


    #Ask for user input
    resort = input("Which ski resort forecast would you like to view? \nSnoqualmie Pass\nStevens Pass\nCrystal Resort\nMt Baker\n-->").lower()
    #List of valid resorts
    valid_resorts = ["snoqualmie pass", "stevens pass", "crystal resort", "mt baker"]
    #check validity
    if resort in valid_resorts:
        pass
    else:
        sys.exit("Ski resort entered is not valid, please restart the program.")


    #Get data
    data = weather_data(resort)


    #Find high and low temperatures for the week
    high, high_date, low, low_date = find_high_temp(data)
    print()
    print(f"The high this week will be {high} degrees Fahrenheit on {high_date}")
    print(f"The low will get down to {low} degrees Fahrenheit on {low_date}")
    print()


    #Find preciptation report for the week
    threshold, precipitation_report = precipitation(data)
    #Print the results
    if not precipitation_report: #If nothing above the threshold...
        print(f"There is no precipitation in the current forecast above a {threshold} percent chance.")
    else:
        #Find length of forecast
        forecast_length = len(precipitation_report)
        #Print each day that is above the threshold
        for i in range(forecast_length):
            values = precipitation_report[i]
            print(f"On {values['date']} there is a {values['probability']} percent chance of precipitation. Here is the detailed forecast description:\n {values['description']} \n")









    

if __name__ == "__main__":
    main()

