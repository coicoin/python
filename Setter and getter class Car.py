#make class Car
class Car():
    #make constructor of class Car
    def __init__(self, year):
#       self.__year = year не подходит поэтому присваиваем set
        self.set_year(year)
    #make properties of model
    def get_year(self):
        return self.__year
    #setter for creating properies
    def set_year(self, year):
        if year < 1900:
            self.__year = 1900
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year


try:
    enter_year = int(input("Введите год машины "))
    car_a = Car(enter_year) #устанавливаем значение года через setter
    print (car_a.get_year()) #получаем значение через getter
    
        
except ValueError:
    print("Введено не целочисленное значение")
#car_a.set_year(2020) #установаливаем значение года через setter
#print (car_a.get_year()) #получаем значение через getter
