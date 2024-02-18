#Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
#четные, потом нечётные

from random import randint
n = int(input("n: "))
A = []
B = []
for i  in range(n):
    A.append(randint(0, 100))
print(A)
for i in range(0, n):
    if A[i] % 2 == 0:
        B.insert(0, A[i])
    else: B.append(A[i])
print(B)

