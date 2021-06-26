#import module
from geopy.distance import geodesic

# Loading the lat-long data for Nairobi & Cairo
Cairo = (30.0444, 31.2357)
Nairobi_city= (1.2921, 36.8219)
  
# Print the distance calculated in km
print(geodesic(Cairo, Nairobi_city).km,"km")