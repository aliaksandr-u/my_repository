#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
#способами
text = input("Введите текст: ")
print(text.replace((" "), ("-")))

a = text.split()
text_1 = '-'.join(a)
print(text_1)