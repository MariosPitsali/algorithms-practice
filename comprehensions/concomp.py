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
meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
        print(meal)
    else:
        print("meal was skipped", meal, sep=" ")
# if in a list comprehension is used as a filter, it cant be used as en if-elif-else clause
f = [meal for meal in menu if "spam" not in meal ]
print (f)
print (meals)
print (meals == f)
print ()