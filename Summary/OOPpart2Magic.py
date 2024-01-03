#Магические методы


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter


c = Counter()
c()


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)
    def __abs__(self):
        return list( map(abs, self.__coords) )


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60  # секунды
        m = (self.seconds // 60) % 60  # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds


        return Clock(self.seconds + other)


    #__eq__() – для равенства ==
    #__ne__() – для неравенства !=
    #__lt__() – для оператора меньше <
    #__le__() – для оператора меньше или равно <=
    #__gt__() – для оператора больше >
    #__ge__() – для оператора больше или равно >=

    class Clock:
        __DAY = 86400  # число секунд в одном дне

        def __init__(self, seconds: int):
            if not isinstance(seconds, int):
                raise TypeError("Секунды должны быть целым числом")
            self.seconds = seconds % self.__DAY

        def get_time(self):
            s = self.seconds % 60  # секунды
            m = (self.seconds // 60) % 60  # минуты
            h = (self.seconds // 3600) % 24  # часы
            return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

        @classmethod
        def __get_formatted(cls, x):
            return str(x).rjust(2, "0")

        def __eq__(self, other):
            if not isinstance(other, (int, Clock)):
                raise TypeError("Операнд справа должен иметь тип int или Clock")

            sc = other if isinstance(other, int) else other.seconds
            return self.seconds == sc


#Если объекты a == b (равны), то равен и их хэш.
#Если равны хеши: hash(a) == hash(b), то объекты могут быть равны, но могут быть и не равны.
#Если хеши не равны: hash(a) != hash(b), то объекты точно не равны.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __len__(self):
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        return self.x == self.y


    #__getitem__(self, item) – получение значения по ключу item;
    #__setitem__(self, key, value) – запись значения value по ключу key;
    #__delitem__(self, key) – удаление элемента по ключу key.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        del self.marks[key]


#__iter__(self) – получение итератора для перебора объекта;
#__next__(self) – переход к следующему значению и его считывание.

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        self.value_row = 0
        return self

    def __next__(self):
        if self.value_row < self.rows:
            self.value_row += 1
            return iter(self.fr)
        else:
            raise StopIteration
