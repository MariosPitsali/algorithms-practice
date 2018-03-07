# cities = ["New York", "Athens", "Belgrade", "Prague"]

# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print (city, file=city_file)
cities=[]
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city)
print (cities)

for city in cities:
    print (city)

    
