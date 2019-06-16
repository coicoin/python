"""
#род.класс транспорт
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")

#производный класс Car
class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса")

#создаем производный класс велосипед, класс велосипед, наследует транспорт
class Cycle(Vehicle):
    def cycle_method(self):
        print("Это дочерный метод из класса Cycle")

car_a = Car()
car_a.vehicle_method() #вызываем метод из дочернего класса
car_a.car_method()
cycle_a = Cycle()
cycle_a.cycle_method()
cycle_a.vehicle_method()
"""

"""
class Car:
    def __init__(self):
        print("Двигатель заведен")
        self.model = "LADA"
        self.__madein = "Россия"
        self._year = 2000

car_a = Car()
print(car_a.model)
#print(car_a.__madein)
print(car_a._year)
"""

"""
class Car:
    message1 = "Двигатель заведен"

    def start(self):
        message2 = "Автомобиль заведен"
        return message2
car_a = Car()
print(car_a.message1)
print(car_a.start()) #не работает message2
"""

"""
#выводит количество созданных машин
class Car:

    car_count = 0
    color = "Blue"

    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)

car_a = Car()
print(car_a.color)
car_b = Car()
car_c = Car()
"""

"""
class Car:

    @staticmethod
    def get_class_details():
        print("Это класс Car")

Car.get_class_details()
"""

"""
#класс, обращаемся через объект
class Car:

    #создаем атрибуты класса
    car_count = 0

    #создаем методы класса, которые увеличивают count на 1 с добавлением объекта.
    def start(self, model, madein, year, color):
        print("Двигатель заведен")
        self.model = model
        self.madein = madein
        self.year = year
        self.color = color
        Car.car_count += 1

print("Поздравляем, ты сотрудник успешной компании! \nУ тебя будет служебный автомоюиль")

#создадим объект т.к. без него работать не будет
car_a = Car()
car_a.start("Mercedes Benz", "Germany", 2019, "Black")
print(car_a.model)
print(car_a.car_count)

car_b = Car()
car_b.start("Москвич 412", "Россия", 1987, "Orange")
print(car_b.model)
print(car_b.car_count)
"""

"""
#Создаем класс car
class Car:

    #создаем атрибуты класса
    model = "Mersedes-Benz"
    madein = "Germany"
    year = 2008
    color = "Dark"

    #создаем методы класса
    def start(self):
        print ("Заводим двигатель")

    def stop(self):
        print ("Глушим двигатель")
#Создаем объект класса Car под названием car_a
car_a = Car()

#Создаем объект класса Car под названием car_b
car_b = Car()

print(dir(car_b))

command1 = 0
i = 0
while command1 != "e":
    command1 = input("Вы в автомобиле, нажмите 'e' чтобы запустить двигатель \n")
    i = i + 1
    if i > 5 and i < 10:
        print("Не заводится!")
    elif i > 2 and i <= 5:
        print("CHECK")
    elif i >= 10:
        print("Аккумулятор сел")
else:
    if i < 10:
        print(car_a.start())
"""
