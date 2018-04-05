# *args is the unpacked tuple
def average(*args):
  print (type(args))
  print ("args is :{}".format(type(args)))
  print ("*args is :", *args)
  mean = 0
  for arg in args:
    mean += arg
  return mean/len(args)

print (average(2,5,6,7,8,10,29))