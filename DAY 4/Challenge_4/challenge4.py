from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent = "geoapiExercises")
location = geolocator.geocode("Mombasa")

print(location)