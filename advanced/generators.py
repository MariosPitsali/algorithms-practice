#python generators save memory
#how to measure memory used in python
import sys

def my_range(n: int):
    start = 0
    print ("function has started counting")
    while start < n:
        print ("my_range is returning {}".format(start))
        yield start
        start += 1
#big_range = range(10000)
#print(big_range)
big_range = my_range(5)
_ = input("line 15")
print(next(big_range))
print ("big range is {} bytes in size".format(sys.getsizeof(big_range)))
#create list that contains all avalues in range
big_list = []
_ = input("line 20")
for val in big_range:
    _ = input("line 23 - inside loop")
    big_list.append(val)
print ("big list is {} bytes in size".format(sys.getsizeof(big_list)))