# # #dictionaries are UNORDERED  
# # dict = {"easy": "easy,peasy lemon squeezy", "difficult": "difficult, difficult lemon difficult"}

# # print ("When you think everything is going to be {} but instead it's {}".format(dict["easy"], dict["difficult"]))

# # cars = {"Porsche": "a sports car that makes women mad", "Ford": "a utilitarian vehicle", "VW":"nevermind the scandal, still very efficient"}


# # while True:
# #   dict_key = input('Please enter a car brand: ')
# #   if dict_key == "quit":
# #     break
# #   if dict_key in cars:
# #     description = cars.get(dict_key)
# #     print (description)
# #   else:
# #     print ("We don't have that car")
# #     

# wraia_koritsia = {"elena": "me mia elia sto magoulo", "polyxeni": "total bitch", "georgia": "o prwtos erwtas", "iwanna": "katourithika"}
# dict_keys = wraia_koritsia.keys()
# wraia_koritsia["omadarxisa"] = "apisteuth"


# print (dict_keys)
# w_tuple = tuple(wraia_koritsia.items())
# print (w_tuple)

# for s in w_tuple:
#     girl, description = s
#     print ("{0} happened with {1}".format(description,girl))

# #make the tuple into a dict again
# print (dict(w_tuple))
# 
 
new_list = ["a", "b", "c", "d"]

new_string = ""
for item in new_list:
    new_string += item + ", "
print (new_string)

t = ["a", "b", "c"]
ty = tuple(t)
newString = "oiordaniseinaienasilithioskaivlakas"
new_string = ", ".join(newString)
print (new_string)

ty = tuple(newString)
print (ty)

oikogeneia = ("Marios", "Iordanis", "Pitsalidis", "Apostolou", "Aggelikhs"), ("Dhmhtrhs", " ", "Pitsalidis", "Apostolou", "Aggelikhs")

for item in oikogeneia:
    name, second, surname, father, mother = item
    print (name, surname)