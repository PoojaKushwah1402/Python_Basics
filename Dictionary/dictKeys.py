car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change dict_keys(['brand', 'model', 'year', 'color']) 