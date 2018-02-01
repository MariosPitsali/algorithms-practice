# #tuples
# import statistics
# t = "a", "b", "c"
# print (t)
# print ("a","b","c")
# print (("a", "b", "c"))

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974

# print (welcome)
# print (welcome[0])
# #tuples are immutable, cant change elements

# #welcome[1]= "Biffy Clyro"
# metallica = "Master of Puppers", "Metallica", 1986

# print (metallica)

# #metallica = metallica[1], metallica[1], 1987
# #metallica [0] = "masd"
# print(metallica)
# #unpacking the tuple
# album, artist, year = metallica
# print (album)
# print(artist)
# print(year)

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

album, artist, year, tracks = imelda
print(album, ", " , artist, ", ", year)
for track in tracks:
    no, title = track
    print ("\t No { } , song { }".format(no, title))
                                             
