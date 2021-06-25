#import module
from geopy.geocoders import Nominatim

#initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

place = "10400 Kenya"

location = geolocator.geocode(place)
print(location)

