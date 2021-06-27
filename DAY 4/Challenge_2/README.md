#**CALCULATE DISTNCE BETWEEN CAIRO AND NAIROBI**

First things first you have to install the Geopy module:
```python
pip3 install geopy
```

##**Approach**
###**Step 1: Import python module**
```python
# import module
from geopy.distance import geodisc
```
###**Step 2: Calculate distance**
```python
Cairo = (30.0444, 31.2357)
Nairobi_city= (1.2921, 36.8219)
print(geodesic(Cairo, Nairobi_city).km,"km")
```
