import constants as constants
import requests

# ** Declare base URL to call

baseURL = "https://api.weatherapi.com/v1/"

# ** Declare an empty variable URL
# ? This is the final URL to which the call is made

URL = ""

# ** Append the mode, key and location query holder to URL

URL = baseURL + "current.json?key=" + constants.WEATHER_API_KEY + "&q="

# ** Choose the location

location = input("Enter location: ")

# ** Append location to the URL

URL += location

# ** Send request

response = requests.get(URL)

# ** Format the JSON response

data = response.json()

if (response.status_code >= 200 and response.status_code < 300):
  print("Current condition in", location, "is:", data['current']['condition']['text'])
else:
  print("Enter the location properly")