A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubblesort(list):
    indexing_length = len(list)-1
    sorted = False 
    
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list[i] > list[i+1]:
                sorted = False
                list[i] , list[i+1] = list[i+1] , list[i]
    return list
    
print(bubblesort(A))
