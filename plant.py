import base64

file = "C:/Users/DELL/Pictures/PotatoEarlyBlight1.jpg"
image = open(file, 'rb')
image_read = image.read()
image_64_encode = base64.encodebytes(image_read)  # encodestring also works aswell as decodestring

print('This is the image in base64: ' + str(image_64_encode))
import requests

url = "https://plant-disease-detector-pytorch.herokuapp.com/"
imgdata = str(image_64_encode)
r = requests.post(url, json={"image": imgdata})
print('hi good')
print(r.text.strip())
