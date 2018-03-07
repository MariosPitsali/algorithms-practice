# #a program to open the random text 
# lorem = open("randomtext.txt")
# for line in lorem:
#     if "ipsum" in line.lower():
#         print (line, end="\t")
# lorem.close()
#
with open("randomtext.txt") as lorem:
    lines = lorem.readlines()
print (lines)

for line in lines:
    print (line, end="")