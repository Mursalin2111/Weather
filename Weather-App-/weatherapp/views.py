from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'DHAKA'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=11a79ea4dd172dfb0eeaa9e126c7e4bf'
    PARAMS = {'units':'metric'}

    API_KEY =  'AIzaSyB2monOFFVgybKomLIiPa7oYQPqCaPc2Ic'

    SEARCH_ENGINE_ID = '466d2cb93292445b4'
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    # Try to get city image from image service
    try:
        # Use LoremFlickr service which provides real images based on keywords
        image_url = f'https://loremflickr.com/1920/1080/{city}'
    except Exception as e:
        # Fallback to a generic landscape image
        image_url = 'https://loremflickr.com/1920/1080/landscape'
    
    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'DHAKA' , 'exception_occurred':exception_occurred } )
               
    
    