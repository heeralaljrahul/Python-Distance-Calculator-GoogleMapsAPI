from asyncio.windows_events import NULL
from tokenize import Double
import requests
import json

# insert your API key here
API_KEY = ""

payload = {}
headers = {}

# Variables for the headers
place1 = input("Please enter place1:")
area1 = input("Please enter area1:")

place2 = input("Please enter place2:")
area2 = input("Please enter area2:")

# replaces the spaces
place1.replace(" ", "%20")
area1.replace(" ", "%20")

place2.replace(" ", "%20")
area2.replace(" ", "%20")

# The URL along with the key, and places
url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+place1 + \
    "%2C%20"+area1+"&destinations="+place2 + \
    "%2C%20"+area2+"&units=imperial&key="+API_KEY

response = requests.request("GET", url, headers=headers, data=payload)
json_object = json.loads(response.text)
# print(response.text)

# turn reponse to string
obj = json_object['rows']
obj = str(obj)
if obj is NULL:
    print("Error")
else:
    print()
    print("----------------------------------")
    # based on the returned output, used string maniupulation to return the distance (had problems using keys)
    distanceString = obj[int((obj).find("text")):int((obj).find("}"))]
    distanceString = distanceString[int(
        (distanceString).find(":")):int((distanceString).find(","))]
    distanceString = distanceString[int(
        (distanceString).find(" ")):int((distanceString).find("mi"))]
    distanceString = distanceString[int(
        (distanceString).find("'")+1):len(distanceString)-1]

    # Display the output
    print("The distance between " + place1 + ' and ' + place2 + " is:")
    print(distanceString+'miles')
    floatDistance = float(distanceString)
    distanceInKM = round((floatDistance*1.60934), 2)
    print(str(distanceInKM)+'km')
