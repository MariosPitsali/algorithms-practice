farm_animals = {"sheep", "cow", "hen"}
print (farm_animals)

for animal in farm_animals:
    print (animal)
    
wild_animals = set(["tiger", "elephant", "lion", "crocodile"])
print (wild_animals)

wild_animals.add("horse")
farm_animals.add("horse")
#as we see in the print result, sets are unordered
print (farm_animals)
print (wild_animals)

# #to create an empty set, dont use {} but set()
# new_set = set()
# new_set.add("a")
# print (new_set)

# newRange = range(0,40,2)
# new_set2 = set(newRange)
# print (new_set2)

# even = set(range(0,40,2))
# print (even)
# print (len(even))

# squares_tuple = (4,9,16,25)
# squares = set(squares_tuple)
# print (squares)
# print (len(squares))

# new = squares.union(even)
# new2 = squares.intersection(even)
# print (new, new2)

# even = set(range(0,40,2))
# squares = set((4,6,9,16,25,36))

# print (sorted(even - squares ))
# even.discard(36)
# even.remove(34)
# print (even)

# odd = set(range(1,41,2))
# if (squares.issubset(even)):
#     print ("Squares is a subset of even")
# if (even.issuperset(squares)):
#     print ("Even is a superset of squares")

even = frozenset(range(0,100,2))
print (even)

even2 = set(range(0,100,2))
even2.add(89)
print (even2)

even2.discard(40)
print (even2)