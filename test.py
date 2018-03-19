from characters import Player

jordan = Player("marios")
print (jordan.lives)
print (jordan.level)
#takes advantage of __str__ function
print (jordan)

jordan._set_lives(5)
print (jordan)

jordan._set_lives(-1)
print (jordan)