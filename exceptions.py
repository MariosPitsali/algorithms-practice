def factorial(n):
    #n! can also be defined as n* (n-1) and calculates n recursively
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)
try:
    print (factorial(3))
except (RecursionError, ZeroDivisionError):
    print ("This programm cannot calculate factorials that large")
# except ZeroDivisionError:
#     print("What are you doing dividing by zero?")
print ("Factorial terminated")