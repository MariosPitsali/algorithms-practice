# 
dict = {}
with open('graph_example_2.txt', 'r') as graph_file:
    for line in graph_file:
        lst = line.split()
        if lst[0] not in dict:
            dict[lst[0]] = []
        if lst[1] not in dict[lst[0]]:
            dict[lst[0]].append(lst[1])
    print (dict)
