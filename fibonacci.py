def fibinacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current+ previous, current
        
        
fib = fibinacci()

print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))
print (next(fib))