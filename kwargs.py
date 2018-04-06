#kwargs comes from key word arguments
def print_backwards(*args, **kwargs):
    print (kwargs)
    for arg in args[::-1]:
        if 'end' not in kwargs.keys():
            print (arg[::-1], end= " ", **kwargs)
        else:
            print (arg[::-1], **kwargs)
with open("backwards.txt", 'w') as backwards:
    print (print_backwards("awesome", "jello", "shot", end= "\n"))
    
print (print_backwards("awesome", "jello", "shot", end= "\n", sep="|"))
