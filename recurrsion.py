import base64
import requests

# encode image to base64
with open("C:/Users/DELL/Pictures/maize.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]

your_api_key = "yaGZP9gxqarQq6ayjg7f3sBqPd88a7J30pcr7PfvijnDvPYtSw"
json_data = {
    "images": images,
    "modifiers": ["similar_images"],
    "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
}

response = requests.post(
    "https://api.plant.id/v2/identify",
    json=json_data,
    headers={
        "Content-Type": "application/json",
        "Api-Key": your_api_key
    }).json()

print(response)

for suggestion in response:
    print(suggestion)