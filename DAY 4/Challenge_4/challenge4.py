from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "geoapiExercises")
country = geolocator.geocode("Mombasa")

print(country)