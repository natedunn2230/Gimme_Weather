import geopy

geolocator = geopy.Nominatim(user_agent="Weather_Twitter_Bot")

def find_coordinates(address):
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)