# from characters import Player

# jordan = Player("marios")
# print (jordan.lives)
# print (jordan.level)
# #takes advantage of __str__ function
# print (jordan)

# jordan._set_lives(5)
# print (jordan)

# jordan._set_lives(-1)
# print (jordan)

from enemy import Enemy, Troll, Vampyre

random_monster = Enemy("Basic Enemy", 12, 1)
random_monster.take_damage(4)
random_monster.take_damage(9)
print (random_monster)

# ugly_troll = Troll()
# print ("Ugly Troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print ("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
brother = Troll("Urg")
print ("Brother troll - {}".format(brother))
vlad = Vampyre("Vlad")
vlad.take_damage(5)
print (vlad)

print ("*" * 40)
another_troll.take_damage(30)
print (another_troll)

while vlad.alive:
    vlad.take_damage(1)
    print (vlad)