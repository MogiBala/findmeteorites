import requests

resp = requests.get("https://data.nasa.gov/resource/y77d-th95.json")
output = resp.text
print (output)