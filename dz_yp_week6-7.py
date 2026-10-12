import json

with open("users.json", "r", encoding = "utf-8") as f:
    users = json.load(f)

cities = {}
for user in users:
    city = user["address"]["city"]
    name = user["name"]
    cities.setdefault(city, []).append(name)

with open("cities.json", "w", encoding = "utf-8") as f:
    json.dump(cities, f, ensure_ascii = False)

print("Словарь записан в cities.json")
print("cities.json:")
print(cities)

