#Создание класа и обьекта
class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, self.age, self.isHappy)


cat1 = Cat()
cat1.name = 'Rasty'
cat1.age = 5
cat1.isHappy = True

cat2 = Cat()
cat2.name = 'Black'
cat2.age = 3
cat2.isHappy = False

cat3 = Cat()
cat3.set_data('Nikky', 8, True)

print(cat1.name)
print(cat2.name)
print(cat3.name)

cat1.get_data()
cat3.get_data()

#Конструкторы
class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, self.age, self.isHappy)


cat3 = Cat('Nikky', 8, True)
cat3.get_data()

#Наследование, инкапсуляция, полиморфизм
class Building:
    __year = None
    __city = None


    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print(self.year, self.city)

class School(Building):
    person = None
    def __init__(self, person, year, city):
        super(School, self). __init__(year, city)
        self.person = person
    def get_info(self):
        print(self.year, self.city, self.person)

school = School(199, 2000,'NY')
school.get_info()
house = Building(2000, 'LA')
house.get_info()
shop = Building(2020, 'NJ')
shop.get_info()

#Создание обьекта на лету - setattr()
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048 #присваиваем новое значение
setattr(Goods, 'inflation', 100)

class Car:
    pass

setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__["color"])

#Функция getattr() возвращает значение атрибута указанного объекта object по его имени name.
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

print(getattr(Notes, 'author'))


class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, 'rus_word', False))


