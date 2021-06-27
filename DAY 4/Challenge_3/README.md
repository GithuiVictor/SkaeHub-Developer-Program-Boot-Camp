#**GET CITY, STATE AND COUNTRY OF A GIVEN LATITUDE USING THE GEOPY PACKAGE & NOMINATIM API**

First things first you have to install the Geopy module:
```python
pip3 install geopy
```

##**Approach**
###**Step 1: Import python module**
```python
# import module
from geopy.geocoders import Nominatim
```
###**Step 2: Initialize the Nominatim API**
Making a nominatim object and initialize Nominatim API with the *geoapiExercises* parameter
```python
geolocator = Nominatim(user_agent="geoapiExercises")
```
###**Step 3: Get city, state and country**
Making a nominatim object and initialize Nominatim API with the *geoapiExercises* parameter
```python
# to capture Latitude & Longitude
location = geolocator.reverse(location_corrdinate, exactly_one=True)
address = location.raw['address']

# traverse the data
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
```
