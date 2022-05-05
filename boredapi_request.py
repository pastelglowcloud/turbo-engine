import requests
import json

page = requests.get("https://www.boredapi.com/api/activity")
print(type(page))
print(page.text[:150]) #print the first 150 characters
print(page.url) #print the url that was fetched
x = page.json() #turn page.text into a python object
print(type(x))
print(json.dumps(x, indent=2)) #pretty print the results