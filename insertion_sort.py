#insertion sort algorithm
#input: an unsorted list of items
#output: a sorted list of items

def insertion_sort(list):
    count = 0
    counttwo = 0
    for i in range(len(list)):
        j = i
        counttwo += 1
        while j>0 and compare(list, j-1, j)>0 :
            #swaps items in list
            swap(list, j-1, j)
            #decrement j by 1
            j = j-1
            #keep count of iterations for alg. complexity
            count += 1
    print (list)
    print (count+counttwo)
def swap (list, a, b):
    list[a], list[b] = list[b], list[a]

def compare(list, a, b):
    return (list[a] - list[b])

insertion_sort([0,1,2,3,4,5,14,10,29,98])