#this is an attempt to recreate the word-guessing game "Hangman"
#will try to be as faithful to the original as possible

import random

dict = {
    0: "___  ",
    1: "| O  ",
    2: "|\|/ ",
    3: "| |  ",
    4: "|/ \ ",
    5: "_dead_"
}
def jas(word_string):
    word_lst = list(word_string)
    word_lst[i] = guess
    word_string = "".join(word_lst)
    return (word_string)
words = ["dangerous", "harem", "uninterrupted", "begging", "antisocial", "carnivore", "veganism", "creation"]
num = random.randint(0,len(words)-1)

word = words[num]
word_string = "_"*len(word)
print(word_string)
trys = 0
while word_string != word:
    
    guesses = []
    guess = input("Please guess a letter, or print quit to exit : ")
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
                trys += 1
                print("Wrooong! {} tries left".format(6-trys))
                for i in range(trys):
                    print (dict[i])
        else:
            print("You have already guessed this one!")
    if trys == 6:
        print("The word was {}. Please try again some other time".format(word))
        break
else:
    print("Congratulations! The word is {}".format(word))

