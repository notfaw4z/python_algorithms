#Function that return each item from the list along with the number of times it appears in the list
A = [1,2,1,3,4,4]

def arraycounts(list):
    map = {}
    for item in list:
        if item in map.keys():
            map[item] += 1
        else:
            map[item] = 1
    return map
        
print(arraycounts(A))
