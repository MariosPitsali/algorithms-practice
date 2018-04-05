#kwargs comes from key word arguments
def print_backwards(*args):
    for arg in args[::-1]:
        print (arg[::-1], end = ' ')

print (print_backwards("awesome", "jello", "shot"))