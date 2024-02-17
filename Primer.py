#Вывести первые N цисел кратные M и больше K
N = int(input("N: "))
M = int(input("M: "))
K = int(input("K: "))
i = 1
j = 1
while i <= N:
    if j * M > K:
        print(j * M)
        i = i + 1
        j = j + 1
    else:
        j = j + 1