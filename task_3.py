#Вывести четные числа от 2 до N по 5 в строку
N = int(input("N: "))
i = 2
for i in range(2, N+1, 2):
    print(i, end=" ")
