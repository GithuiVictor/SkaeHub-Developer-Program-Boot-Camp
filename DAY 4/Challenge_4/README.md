#**GET COUNTRY NAME OF A GIVEN STATE USING THE GEOPY PACKAGE & NOMINATIM API**

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
###**Step 3: Get Country Name**
```python
country = geolocator.geocode("Mombasa")
```
