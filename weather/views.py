
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def weather(request):
    
    if request.method == 'POST':
        city = request.POST.get('city')
        if city=="":
            return redirect("/weather/")

        # source contain JSON data from API
    
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=6c9d151653b1b990d22313b234195113').read()

         # converting JSON data to a dictionary
        #import pdb; pdb.set_trace()
        list_of_data = json.loads(source)
  
        # data for variable list_of_data
        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data ={}
    return render(request, "weather.html", data)
