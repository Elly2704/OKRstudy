from dataclasses import dataclass, field, InitVar


class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


#type(<имя класса>, <кортеж родительских классов>, <словарь с атрибутами и их значениями>)
#A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})


#def create_class_point(name, base, attrs):
    #attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    #return type(name, base, attrs)

class Meta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta): #create_class_point
    def get_coords(self):
        return (0, 0)

# API ORM Django

class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name_class, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women:
    class_attrs = {'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото'}
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

#Data classes

class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing: {self.__dict__}"

#Тоже самое только через Dataclassed

@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list) #создание изменяемого обьекта

class Vector3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5

#Метод __post_init__()
@dataclass
class V3D:
    x: int
    y: int
    z: int
    calc_len: InitVar[bool] = True
    lenght: float = field(init=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
         self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5




