# pip  install geopy

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse("37.4224764, -122.0842499")

print(f"Address: {location.address}")
print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")

from geopy.distance import geodesic

address1 = "1600 Amphitheatre Parkway, Mountain View, CA"
address2 = "1 Infinite Loop, Cupertino, CA"

location1 = geolocator.geocode(address1)
location2 = geolocator.geocode(address2)

coord1 = (location1.latitude, location1.longitude)
coord2 = (location2.latitude, location2.longitude)

distance = geodesic(coord1, coord2).km

print(f"Between {location1.address} and {location2.address}: \nDistance : {distance:.2f} km")


# output
# Address: Amphitheatre Parkway, Mountain View, Santa Clara County, California, 94043, United States
# Latitude: 37.42265085, Longitude: -122.0836528633059
# Between Google Headquarters, 1600, Amphitheatre Parkway, Mountain View, Santa Clara County, California, 94043, United States and Infinite Loop 1, 1, Infinite Loop, Apple Campus, Cupertino, Santa Clara County, California, 95014, United States:
# Distance : 11.10 km