# In an early video, we used a for loop to print the times tables, for values from 1 to 10.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.
import timeit
import time
loop1= """ 
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)""" 
loop2 = """ 
for x,y in [(i, i*j) for i in range(1,11) for j in range(1,11)]:
    print (x, y)"""
result1 = timeit.timeit(loop1, globals=globals(), number =100) 
print (result1)
time.sleep(3)
result2 = timeit.timeit(loop2, globals=globals(), number=100)
print (result2)
