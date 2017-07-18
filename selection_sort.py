# input : a list of items to be sorted
# output: a sorted list

#selection sort algorithm
list = [1,5,2,8,14,3,7,9,6,4]
def compare(a, b):
    return (a-b)

def swap(lst, a, b):
    c = lst[a]
    d = lst[b]
    lst[a] = d
    lst[b] = c
def selection_sort(list):    
    for i in range(0, len(list)-1):
        m = i
        for j in range(i+1, len(list)):
            result = compare(list[j], list[m])
            if result < 0:
                m = j
        if i != m:
            swap(list, i, m)
    print (list)

selection_sort(list)

