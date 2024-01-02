from accessify import private, protected

class Point:
    'Описание класса'
    color = 'red'
    circle = 2
    def __new__(cls, *args, **kwargs):
        print('New' + str(cls))
        return super().__new__(cls)

    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

    def __del__(self): #сборщик мусора
        print('Delete' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
pt.set_coords(1, 2)

pt1 = Point(10, 20)

print(pt.__dict__, pt1.__dict__)




Point.__dict__

a = Point()
isinstance(a,Point)
True

setattr(Point, 'type', 'line') #  добавить атрибут в класс

getattr(Point, 'a', False) #если атрибута нет
False

hasattr(Point, 'type')
True #наличие атрибута

del Point.circle # удалить атрибут
delattr(Point, 'type')


Point.__doc__
'Описание класса'


#Singelton
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


db = DataBase('root', '1234', '4321')
db2 = DataBase('root2', '12341', '43214')

print(id(db), id(db2)) # они равны, т.к создался один обьект, а при создании второго он заменит первый

#Декораторы методов класса @classmethod и @staticmethod


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MAX_COORD >= arg >= cls.MIN_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


print(Vector.norm2(5 ,8))

#Основа инкапсуляции

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @private# = __, но более защищен
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_сoord(self):
        return self.__x, self.__y

pt = Point(1, 2)



#attribute (без одного или двух подчеркиваний вначале) – публичное свойство (public);
# _attribute (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри
# класса и во всех его дочерних классах)
# __attribute (с двумя подчеркиваниями) – режим доступа private (служит для обращения только внутри класса).

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)



#Паттерн моносостояние

class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old


    def get_old(self):
        return self.__old


    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)


p = Person('Сергей', 20)
print(p.old)

#Тоже самое только через декоратор


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_weight()
        self.verify_ps()
        self.verify_old()

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14; 120]")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
         return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps




#Дескрипторы

class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord

p = Point3D(1, 2, 3)
print(p.__dict__)



