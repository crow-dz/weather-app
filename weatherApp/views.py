from django.shortcuts import render
from .forms import theCity
import requests
import datetime
from django.utils.timezone import utc


def home(request):
	form = theCity(request.POST)
	if form.is_valid():
		city = form.cleaned_data.get('city')
		try:
			api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
			url = api_address + city
			json_data = requests.get(url).json()
			# name
			name = json_data['name']
			# temp
			temps = json_data['main']['temp'] 
			temp = int(temps-273.15)
			# humidity
			humidity = json_data['main']['humidity']
			# wind
			wind = json_data['wind']['speed']
			#weather
			weather = json_data['weather'][0]['description']
			#icon
			icon = json_data['weather'][0]['icon']
			# icon url
			urli ='http://openweathermap.org/img/wn/'+icon+'@2x.png'
			timeNow = datetime.datetime.utcnow().replace(tzinfo=utc)
			timenow=timeNow.strftime("%b,%d %I:%M %p")
			context={'form':form,'name':name,'temp':temp,'humidity':humidity,'wind':wind,'weather':weather,'urli':urli,'time':timenow}
		except:
			feed = 'There is no city such name .'
			context={'form':form,'feed':feed}
	else:
		form = theCity()
		context={'form':form}

	return render(request,'base.html',context)