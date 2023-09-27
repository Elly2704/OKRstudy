# Функция в python - объект, принимающий аргументы и возвращающий значение. Обычно функция определяется с помощью
# инструкции def. (но может быть без аргументом и знавчение не возвращать)
# def <имя функции>([список аргументов]):
#        оператор 1
#        оператор 2
#        …
#        оператор N
def add(x, y):
    return x + y
# Инструкция return говорит, что нужно вернуть значение
def test_func(word):
    print(word)
test_func('Hi')

def summa(a,b):
    res = a + b
    return res
el = summa(5,9)
print(el)

def mini(l):
    minn = l[0]
    for el in l:
        if el <= minn:
            minn = el
    print(minn)

nums2 = [1, 2.1, 3, True]
mini(nums2)

#Треугольник
def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b

# Четное / нечетное
def even(x):
    return x % 2 == 0
while True:
    x = int(input())
    if x == 1:
        break
    if even(x):
        print(x)

def is_large(s):
    return len(s) >= 6
l = input().split()
ls = [x for x in l if is_large(x)]
print(*ls)

#Алгоритм Евклида для нахождения НОД (наибольшего общего делителя двух натуральных чисел)
def get_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

# формальные параметры - это параметры функции со значениями по умолчанию
# именованные аргументы - это значения с дополнительным указанием имени параметра функции
# позиционные аргументы - это передаваемые функции значения, записанные через запятую
# фактические параметры - это позиционные параметры функции без значений по умолчанию
def get_rect_value(a, b, type = 0):
    if type == 0:
        return 2 * (a + b)
    else:
        return a * b

def check_password(passw, chars="$%!?@#"):
    return len(passw) > 7 and True in [m in chars for m in passw if m in chars]

# Функции с произвольным числом параметров
def get_even(*args):
    a = []
    for i in args:
        if i % 2 == 0:
            a.append(i)
    return a

# Рекурсивные функции (это функция, которая вызывает саму себя)
N = int(input())
def get_rec_N(N):
    i = 1
    for i in range(N):
        if i != N:
            print(i + 1)

n = int(input())
def fact_rec(n):
    if n <= 0:
        return 1
    else:
        return n * fact_rec(n-1)

# Анонимные (lambda) функции (к данной функции можно обратиться только в том месте, где она и написана)
lambda <аргументы функции через запятую> : тело функции
func = lambda a, b: a ** b
print(func(4,6))

get_sq = lambda x: x ** 2

# global -  чтобы менять глобальные переменные в локальном окружении (например, внутри функций)
def create_global(x):
    global TOTAL
    TOTAL = x

# nonlocal -  чтобы из одной локальной области обращаться к локальной переменной из внешней локальной области
def func1():
    msg = input()
def func2():
        nonlocal msg
        msg = input()
        print(msg)

# Декораторы в Python представляют функцию, которая в качестве параметра получает функцию и в качестве
# результата также возвращает функцию. Декораторы позволяют модифицировать выполняемую функцию, значения ее
# параметров и ее результат без изменения исходного кода этой функции.
import webbrowser
def validator(func):
    def wrapper(url):
       if '.' in url:
           func(url)
       else:
           print('Non valid URL')
    return wrapper
@validator
def open(url):
    webbrowser.open(url)

open('https://www.youtube.com')

lst = input()
def srt(func):
    def wrapper(args):
        res = sorted(func(args))
        return res
    return wrapper
@srt
def get_list(lis):
    lis = list(map(int, lis.split()))
    return lis
print(*get_list(lst))

def dec(tag = 'h1'):
    def decor(func):
        def coun(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return coun
    return decor
@dec(tag = 'div')
def low(s):
    return s.lower()

s = input()
print(low(s))