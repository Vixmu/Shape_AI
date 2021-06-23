import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("Weather Stats for - {} || {}".format(location.upper(), date_time))

print ("Current temperature : {:.2f} deg C".format(temp_city))
print ("Current weather :",weather_desc)
print ("Current Humidity :",hmdt, '%')
print ("Current windspeed :",wind_spd ,'kmph')

txtdoc=[temp_city,weather_desc,hmdt,wind_spd,date_time]
with open("weather.txt",'w',encoding = 'utf-8')as f:
  f.write("------------------------------------------------------------------------------------------------------------------------------")
  f.write("weather stats for - {} || {}".format(location.upper(),date_time))
  f.write("------------------------------------------------------------------------------------------------------------------------------")
  f.write("current Temperature is: (:.2f) deg (\n".format(txtdoc[0]))

  f.write("{},{}\n".format("Current weather desc :",txtdoc[1]))
  f.write("{} ,{} ,{} \n".format("Current Humidity :",txtdoc[2],"%"))
  f.write("{} ,{} ,{} \n".format("Current wind speed :",txtdoc[3],"kmph"))
  f.write("-------------------------------------------------------------------------------------------------------------------------------")
  f.close