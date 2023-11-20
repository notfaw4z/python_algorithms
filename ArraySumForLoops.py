def arraysum(A, target):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i]+A[j] == target:
                return A[i], A[j]
        	
A = [1,2,3,4,5,123]
target = 8

print(arraysum(A, target))
