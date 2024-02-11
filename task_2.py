#Сделать калькулятор: у пользователя
#спрашивается число, потом действие и второе
#число
a = float(input("Число 1: "))
d = input("Действие: ")
b = float(input("Число 2: "))
if d == "+":
    c = a + b
    print(c)
elif d == "-":
    c = a - b
    print(c)
elif d == "*":
    c = a * b
    print(c)
elif d == "/":
    c = a / b
    print(c)
else:
    print("Недопустимое значение")