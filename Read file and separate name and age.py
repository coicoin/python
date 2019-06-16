import re

class Person:

    def passport(self, name, age):
        self.name = name
        self.age = age
        print("Имя", name, "возраст", age)

#записываем файл
name = str(input("Введите ваше имя "))
age = str(input("Введите ваш возраст "))
f = open("study.txt", "a") #запись в файл
f.write(name + " " + age + "\n")
f.close()

#создание регулярных выражений на поиск цифр и букв
pattern_digit = r"(\d)"
pattern_word = r"(\D)"

#читаем файл
f1 = open("study.txt")
for word in f1:
    file = f1.read().split() #считываем через пробел
    for i in file:
        match_digit = re.match(pattern_digit, i) #поиск цифрового соответствия
        if match_digit:
            dict_age = {"age" : i} #словарь, возрасту присваиваем все значения
            print(dict_age)
    for j in file:
        match_word = re.match(pattern_word, j) #поиск буквенного соответствия
        if match_word:
            dict_name = {"name" : j} #словарь, имени присваиваем все значения
            print(dict_name)
            
#создаем объект ниже, не работает, нужно чтоб вывела весь список имен и возрастов по предложениям
human = Person()
biography = human.passport(dict_name.get("name"), dict_age.get("age"))
biography.passport()
f1.close()
