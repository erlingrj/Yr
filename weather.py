import urllib.request
from datetime import datetime
import xml.etree.ElementTree as ET

url = 'http://www.yr.no/sted/Norge/Tr%C3%B8ndelag/Trondheim/Trondheim/varsel.xml'



def get_weather_today():
    """ This function gets the weather data from Trondheim and return a tuple with
    (symbol, rain, temp, wind). Symbol is an int given a general picture for the given period
    whilst the others are floats and self explanatory"""

    period = []
    symbol = []
    rain = []
    temp = []
    wind = []

    today = datetime.now()
    response = urllib.request.urlretrieve(url, 'weather.xml')
    weatherdata = ET.parse('weather.xml').getroot()

    forecast = weatherdata[5][1]


    for forecast_period in forecast:
        date = forecast_period.get('from').split('T')[0]
        if str(today).split(' ')[0] == date:
            period.append(int(forecast_period.get('period')))
            rain.append(float(forecast_period[1].get('value')))
            temp.append(float(forecast_period[4].get('value')))
            wind.append(float(forecast_period[3].get('mps')))
            symbol.append(int(forecast_period[0].get('number')))
        else:
            break

    return (period,symbol,rain,temp,wind)

if __name__ == '__main__':
    print(get_weather_today())
