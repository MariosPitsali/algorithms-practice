#challenge time

ip = input("Please type in the IP Address: ")
segments = 1
length = 0

for i in range(0, len(ip)):
    if (ip[i] == '.') or (ip[i]==""):
        print ("Segment no. %2d has length %2d" % (segments, length))
        segments += 1
        length=0
    else:
        length += 1
