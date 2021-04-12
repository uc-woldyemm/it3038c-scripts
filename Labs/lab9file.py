import json
import requests

r = requests.get('http://localhost:3000')

data = r.json()

first =(data[0]["name"])
first_ = (data[0]["color"])
print(first + " is " + first_)

second =(data[1]["name"])
second_ = (data[1]["color"])
print(second + " is " + second_)

third =(data[2]["name"])
third_ = (data[2]["color"])
print(third + " is " + third_)

fourth =(data[3]["name"])
fourth_ = (data[3]["color"])
print(fourth + " is " + fourth_)

#Widget is blue
#Widget is green
#Widget whatever is whatever
