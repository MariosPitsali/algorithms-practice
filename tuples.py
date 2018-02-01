#tuples
import statistics
t = "a", "b", "c"
print (t)
print ("a","b","c")
print (("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974

print (welcome)
print (welcome[0])
#tuples are immutable, cant change elements

#welcome[1]= "Biffy Clyro"
metallica = "Master of Puppers", "Metallica", 1986

print (metallica)

metallica = metallica[1], metallica[1], 1987
print(metallica)

ls = list (range(1,100,5))
l = statistics.median(ls)
print (l)