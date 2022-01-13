import requests

freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()

user_postition = [geo_json["latitude"], geo_json["longitude"]]

print(user_postition)
