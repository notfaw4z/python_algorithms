def CommonItemArray(Array1,Array2):
    B = {}
    for item in Array1:
        if item not in B.keys():
            B[item] = 1
    
    for item in Array2:
        if item in B.keys():
            print(item)
    print(B)


CommonItemArray(['a', 'b', 'c', 'x','b'],['z', 'y', 'x'])
