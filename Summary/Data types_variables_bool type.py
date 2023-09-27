#Переменные - ссылка на объект в памяти. Предназначены для хранения данных.
#Название переменной в Python должно начинаться с алфавитного символа или со знака подчеркивания и может содержать
#aлфавитно-цифровые символы и знак подчеркивания.
#И кроме того, название переменной не должно совпадать с названием ключевых слов языка Python.
#Типизация реализована в Python динамическая(переменная не привязана жестко к определенному типу),строгая

# Базовые операции
a = 3
b = 4
c = 8
print(a + b ** c * a)
print(a - b // c / a)
print(8 % 3)
i = 2
i += 3
print(i) # i=5
print('value', 152, 7.5, True, sep='\n')
print(s1, end=' ')
print('value', 152, 7.5, True, min(5, 8, 10, True))
print('value', 152, 7.5, True, max(5, 8, 10, True))
print('value', 152, 7.5, True, abs(5, 8, 10, True))
print('Hi' * 5) # в одну строку
print('Hi\n' * 5) # с переходом на новую
cat, dog = 'red', 'white' #множдественное присваивание
a = b = c = 0 #каскадное присваивание
import math
print(round(math.sqrt(a**2+b**2), 2))
print(round(math.factorial(a)/ (math.factorial(b) * (math.factorial(a -b)))))
print(math.ceil((a+b)/20))

#Приведение типов
integer = 5
float = 5.89
string = 'Hello'
boolean = True/False
print(integer + int(float))
print(string + str(integer + int(float)))
#task
a = int(input('Number 1:'))
b = int(input('Number 2:'))
c = float(input('Number 3:'))
print(a + b ** c)
print(a - b // c)

#Bool
a = float(input())
print(int(a)%3==0)
a, b = map(int, input().split())
print((a % b) == 0)
a = float(input())
print((a >= 0 and a <= 2) or (a >= 10 and a <= 20)) # диапазон [0; 2] или в диапазон [10; 20] (включительно)