dictt = {}
try:
    dictt.items() = [l for l in range(5)]
except SyntaxError as e:
    print (type(e))
    print ("OOps")
