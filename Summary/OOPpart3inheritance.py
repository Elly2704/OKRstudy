#Наследование классов

class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")


p = Geom()

print(issubclass(Line, Geom))
print(isinstance(p, Line))


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


#Полиморфизм

class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]

for g in geom:
    print(g. get_pr())


#Множественное наследование

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()

        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):

        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")


class NoteBook(Goods, MixinLog):
    pass


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

#ограничение создаваемых локальных свойств;
#уменьшение занимаемой памяти;
#ускорение работы с локальными свойствами.

#Обработка исключений


try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
except ValueError:
    print("Ошибка типа данных")


try:
    x, y = map(int, input().split())
    res = x / y
except:
    print("Ошибка")


try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
else:
    print("Исключений не произошло")


try:
    f = open("myfile.txt")
    f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
finally:
    if f:
        f.close()
        print("Файл закрыт")


def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as v:
        print(v)
        return 0, 0
    finally:
        print("finally выполняется до return")


x, y = get_values()
print(x, y)


try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except ZeroDivisionError:
        print("Деление на ноль")
except ValueError as z:
    print("Ошибка ValueError")

# Raise - создание обработки ошибок

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception("принтер не отвечает")

    def send_to_print(self, data):
        return False

