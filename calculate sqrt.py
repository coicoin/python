class Square:

    @staticmethod
    #возведение квадрата
    def get_squares(a, b):

        print("Возведение степени квадрата")
        return a*a, b*b

x = int(input("Введите значение A "))
y = int(input("Введите значение B "))
print(Square.get_squares(x, y))
