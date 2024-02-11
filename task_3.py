#Вывести четные числа от 2 до N по 5 в строку
N = int(input("N: "))
i = 2
while i <= N:
    if i % 2 ==0:
        print(i)
        i = i +1
    else:
        i = i +1