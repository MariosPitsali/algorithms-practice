import sys
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#         print(meal)
#     else:
#         print("meal was skipped", meal, sep=" ")
# # if in a list comprehension is used as a filter, it cant be used as en if-elif-else clause
# f = [meal if "spam" not in meal else "a meal was skipped" for meal in menu ]
# print (f)

# x = 12
# expression = "Twelve" if x == 12 else "unkwown"
# print (expression)

for meal in menu:
    print (meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print ()
items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print (items)
print ()

for meal in menu:
    for item in items:
        if item in meal:
            print ("{} contains {}".format(meal, item))
            break
for i in range(1,31):
    fizzbuzz = "fizz buzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i%2 == 0 else str(i)
    print (fizzbuzz)