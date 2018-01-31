# detect odd and even numbers in random set
import random

list = random.sample(range(0,1000), k=10)
number_of_even = 0
number_of_odd = 0
print(list)
for item in list:
    if item % 2 == 0:
        number_of_even += 1
    else:
        number_of_odd += 1
print("There are %d even numbers and %d odd numbers" %(number_of_even, number_of_odd))



