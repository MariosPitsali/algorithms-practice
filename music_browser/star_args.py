# *args is the unpacked tuple
def average(*args):
  print (type(args))
  print ("args is :{}".format(type(args)))
  print ("*args is :", *args)
  mean = 0
  for arg in args:
    mean += arg
  return mean/len(args)

def build_tuple(*args):
    return args

def find_length(*args):
    lst = [str(arg) for arg in args]
    sum = 0
    for word in lst:
        sum += len(word)
    return sum/len(lst)

def find_min(*args, r_type:str=None):
    return max(args)

def invert(*args):
    return tuple([arg[::-1] for arg in args[::-1]])
# print (average(2,5,6,7,8,10,29))
# print (build_tuple("z",6,"fo sho",5))
# print (type(build_tuple("gs","kl")))

# ls = [5,5,6,4]
# print (ls)
# print (set(ls))
#
print (find_length("jumbotron", "macarena", "mercenary","eggs"))
print (find_min(3,6,9,8,5))
print (invert("hess", "is", "more"))

st = "undermine"
print (st[::-1])