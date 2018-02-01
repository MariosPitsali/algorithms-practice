# #loops

# for i in range(0,11):
#     print ("i is now {}".format(i))

    
# answers = [ "none", "two", "four"]
# name = input("What is your name? ")
# ans = ""
# while (ans not in answers):
#     ans = input("How many backs does a camel have, {}? ".format(name))
#     if ans =="quit":
#         break
# else: 
#     print ("That's correct!")

import random

highest = 1000
answer = random.randint(1, highest)

guess = int(input("Please guess a number from 1 to {} : ".format(highest)))
while (guess != answer):
    if (guess > answer):
        guess = int(input("Please guess lower: "))
    elif (guess < answer):
        guess = int(input("Please guess higher: "))
else:
    print('Congratulations, you guessed it!')