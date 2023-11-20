def arraysum(A, target):
    B = {}
    complement = 0
    for item in A:
        complement = target - item
    
        if item in B.keys():
            print(complement,item)
        else:
            B[complement] = 1
    

A = [1,2,3,4,5,123]
target = 8

print(arraysum(A, target))
