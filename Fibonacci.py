def fibo(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        print(sum, end=" ")
        sum = a+b
        b = a
        a = sum

print(fibo(6))
