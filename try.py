import json
import requests
import configparser
import logging

def getWeather(latitude, longitude):
    config = configparser.ConfigParser()
    config.read("config.ini")
    appid = config['openwweather']['key']
    openweatherapiurl = "https://api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&APPID="+appid
    logging.info("[getWeather] request URL:" + openweatherapiurl)
    try:
        response = requests.get(openweatherapiurl)
        data = response.json()
        logging.info(data)
        answer = data['weather'][0]['description'] + ". Temp:" + str(int(data['main']['temp']-273.15))+ " (High "+str(int(data['main']['temp_max']-273.15))+", low " +str(int(data['main']['temp_min']-273.15))+". Humidity: "+str(data['main']['humidity'])+"\n"
        logging.info("[getWeather]:" + answer)
        return answer
    except:
        return None


{
	"coord": {"lon": 121.57, "lat": 25.04},
	"weather": [
		{"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"}
	],
	"base": "stations",
	"main": {
		"temp": 305.75,
		"pressure": 1005,
		"humidity": 60,
		"temp_min": 303.71,
		"temp_max": 309.15
	},
	"visibility": 10000,
	"wind": {"speed": 7.2, "deg": 280},
	"clouds": {"all": 20},
	"dt": 1560929615,
	"sys": {
		"type": 1,
		"id": 7949,
		"message": 0.0071,
		"country": "TW",
		"sunrise": 1560891849,
		"sunset": 1560941141
	},
	"timezone": 28800,
	"id": 1675720,
	"name": "Xianeibu",
	"cod": 200
}