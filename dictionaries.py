fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": " a small, sweet fruit growing in trees",
         "lime": "a sour, green, citrus fruit"}

print (fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmm, lovely",
       "spinach": "love it"}
#adds the fruit dictionary into veg dictionary
#.update does not *return* a new dictionary
veg.update(fruit)
print (veg)

nnn = fruit.copy()
print (nnn)

