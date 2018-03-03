print ("Please insert a text down below: \t")
string = input("Here:")

vowels = frozenset("aeuio")

wordset = set(string)


print (sorted(wordset.lower().difference(vowels)))