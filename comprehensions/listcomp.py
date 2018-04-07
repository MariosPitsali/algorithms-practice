print (__file__)

numbers = [1,2,3,4,5,6]
#a list comprehensions produces a list
#squares = {number**2 for number in numbers}
squares = [number**2 for number in range(10)]
print (squares)