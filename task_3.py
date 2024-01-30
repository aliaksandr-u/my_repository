#Пользователь вводит Имя, Возраст и Город, сформировать
#приветственное сообщение путем форматирования 3-мя способами
name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")
text = "Привет %s %s из %s" % (name, age, city)
print(text)

text2 = "Привет {} {} из {}".format(name, age, city)
print(text2)

text3 = f"Привет {name} {age} из {city}"
print(text3)