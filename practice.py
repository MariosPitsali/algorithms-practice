# # detect odd and even numbers in random set
# import random

# list = random.sample(range(0,1000), k=10)
# number_of_even = 0
# number_of_odd = 0
# print(list)
# for item in list:
#     if item % 2 == 0:
#         number_of_even += 1
#     else:
#         number_of_odd += 1
# print("There are %d even numbers and %d odd numbers" %(number_of_even, number_of_odd))

# #continue practice

# for i in range(0,7):
#     if (i == 3) or (i == 6):
#         continue
#     print (i)

# n = int(input("Rows: "))
# m = int(input("Columns: "))
# lst = []

# for i in range(0, n):
#     new_lst = []
#     for j in range(0, m):
#         new_lst.append(i*j)
#     lst.append(new_lst)
# for list in lst:
#     print(list, end="\n")
    
    
#new one
sequence = '8'
lst=[]
while( sequence ):
    sequence = input("Please enter sequence: ")
    lst.append(sequence.lower())
    
for seq in lst:
    print(seq)