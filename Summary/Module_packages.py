# Модуль в языке Python представляет отдельный файл с кодом, который можно повторно использовать в других программах.
# Для создания модуля необходимо создать файл с расширением *.py, который будет представлять модуль.
# Название файла будет представлять название модуля. Затем в этом файле надо определить одну или несколько функций.
import math
a = float(input())
print(math.ceil(a))

import datetime as d
print(d.datetime.now())

from math import factorial as fact
def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p

import module #импорт моего модуля
print(module.hello('j'))
print(module.add_nums(1,6,5))

# pip list - отображает список установленных модулей для текущего интерпретатора
# pip freeze > requirements.txt -  создает текстовый файл со списком установленных модулей и номерами их версий
# пакет - это каталог с набором модулей и обязательным файлом __init__.py
