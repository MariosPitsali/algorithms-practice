#this is an attempt to recreate the word-guessing game "Hangman"
#will try to be as faithful to the original as possible

import random

def jas(word_string):
    word_lst = list(word_string)
    word_lst[i] = guess
    word_string = "".join(word_lst)
    return (word_string)
words = ["dangerous", "harem","precious","incredible","peculiar","irreversible", "uninterrupted", "begging", "antisocial", "carnivore", "veganism", "creation"]
num = random.randint(0,len(words)-1)

word = words[num]
word_string = "_"*len(word)
print(word_string)
trys = 0
while word_string != word:
    
    guesses = []
    guess = input("Please guess a letter, or print quit to exit : ").lower()
    if guess == "quit":
            break
    elif len(guess) > 1:
        print ("You only have to guess one letter at a time!")
    else:
        if guess not in guesses:
            guesses.append(guess)
            if guess in word:
                print ("Correct! So... what's your next guess? ")
                for i in range(len(word)):
                    if word[i] == guess:
                        word_string = jas(word_string)
                print(word_string)
            else:
                print("Wrooong! {} tries left".format(5-trys))
                trys += 1
                
        else:
            print("You have already guessed this one!")
        
    if trys == 5:
        print("The word was {}. Please try again some other time".format(word))
        break
else:
    print("Congratulations! The word is {}".format(word))

