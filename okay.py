from geopy.geocoders import Nominatim

geolocator = Nominatim(
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
location = geolocator.reverse("-6.7963, 39.2847")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
