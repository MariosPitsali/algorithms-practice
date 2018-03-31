#exceptions challenge
import sys
def division(n, m):
    return (n/m)

def request_input():
    while True:
        try:
            number =  int(input("Please enter an integer: "))
            #break or return statements get us out of the while loop
            return number
        except ValueError:
            print ("Incorrect entry, please try again")
        except EOFError:
            sys.exit(0)
        finally:
            print ("Finally clause always executes")
try:
    print ("This programm calculates the result of a division between two integers :)\n")
    number1 = request_input()
    number2 = request_input()
    print (division(number1, number2))
    
except ZeroDivisionError:
    print ("Come on now, cannot divide by zero!")
except ArithmeticError:
    print ("Please, only integers")
#code in else block executes only if try block is completed without finding exception
else:
    print ("Division performed successfully")