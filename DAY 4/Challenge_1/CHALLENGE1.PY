#import module
from geopy.geocoders import Nominatim

#initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

#Request for user input of the zip code
zip_code = input("Please enter the zip code of your desired location")

#Get location with the geolocator.geocode() function
location = geolocator.geocode(zip_code)
print(location)

