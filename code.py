import pywapi

city = int(input("Choose your city: \n 1 - Moscow, 2 - Minsk, 3 - Saint-Petersburg, 4 - New York, 5 - London, 6 - Bristol, 7 - Kiev, 8 - Los Angeles, 9 - Jerusalim, 10 - Warsaw.   "))
if city == 1:
    weather_com_result = pywapi.get_weather_from_weather_com('RSXX0063')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Moscow.\n\n")
elif city == 2:
    weather_com_result=pywapi.get_weather_from_weather_com('BOXX0014')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Minsk.\n\n")
elif city == 3:
    weather_com_result=pywapi.get_weather_from_weather_com('RSXX0091')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Saint-Petersburg.\n\n")
elif city == 4:
    weather_com_result = pywapi.get_weather_from_weather_com('USNY0996')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n")
elif city == 5:
    weather_com_result = pywapi.get_weather_from_weather_com('UKXX0085')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in London.\n\n")
elif city == 6:
    weather_com_result=pywapi.get_weather_from_weather_com('UKXX0025')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Bristol.\n\n")
elif city == 7:
    weather_com_result=pywapi.get_weather_from_weather_com('UPXX0486')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Kiev.\n\n")
elif city == 8:
    weather_com_result=pywapi.get_weather_from_weather_com('USCA0638')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Los Angeles.\n\n")
elif city == 9:
    weather_com_result=pywapi.get_weather_from_weather_com('ISXX0010')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Jerusalim.\n\n")
elif city == 10:
    weather_com_result=pywapi.get_weather_from_weather_com('PLXX0028')
    print("Weather.com says: It is " + str(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Warsaw.\n\n")


