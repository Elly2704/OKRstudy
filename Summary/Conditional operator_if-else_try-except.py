# Условные операторы Python IF, ELSE, ELIF. Условный оператор в Python выполняет различные вычисления или действия в
# зависимости от того, оценивает ли конкретное логическое ограничение как true или false.
#Вывести на экран наибольшее из чисел
a, b = map(float, input().split())
if a > b :
    print(a)
else:
    print(b)

# Если введенное слово палиндром, на экран вывести ДА, иначе - НЕТ.
x = list(input().lower())
if x[::] == x [::-1]:
    print('ДА')
else:
    print('НЕТ')

# Деление
m, n = map(int, input().split())
if m % n == 0:
    print(int(m // n))
else:
    print(f'{m} на {n} нацело не делится')

#Возраст пользователя - вложенное условие
user_age = int(input('Your age:'))
if user_age > 18:
    print('You are of legal age!')
elif user_age == 18:
    print('Prove it!')
else:
    print('Grow up more!')

# Наименьшее среди них и вывести его на экран
a, b, c  = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
elif b < c:
    print(b)
else:
    print(c)

#Вывести на экран номер категории, в которой будет выступать боксер.
a = float(input())
if a <= 60:
    print('1')
elif a <= 64:
    print('2')
elif a <= 69:
    print('3')
else:
    print('4')

#Тернарный условный оператор
a = int(input())
d = "кратно 3" if a % 3 == 0 else "не кратно 3"
print(d)

a = str(input()).lower()
a = "палиндром" if a[::] == a[::-1] else "не палиндром"
print(a)

a = int(input())
a = a + 1 if 0 <= a < 59 else 0
print(a) # Секундомер - Вводится текущее время (секунды) в диапазоне [0; 59]. Если значение равно 59,
# то следующее должно быть 0. И так по кругу.

# Конструкция try - except для обработки исключений
# Работа с файлами
data = input('Text: ')
file = open('text.txt', 'w')
file.write(data)
file.close()

file = open('text.txt', 'r')
print(file.read(2))

try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")


data = 0
while data == 0:
    try:
        data = int(input('Number:'))
        data += 5
        print(data)
    except ValueError:
        print('Only numbers')
    finally:
        print('Finally')

# With...as
try:
    with open(text2.txt, 'r') as file:
        print(file.read())
except NameError:
    print('Error')


# BaseException - базовое исключение, от которого берут начало все остальные.
# SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
# KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
# GeneratorExit - порождается при вызове метода close объекта generator.
# Exception - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
#     StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
#     ArithmeticError - арифметическая ошибка.
#         FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
#         OverflowError - возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
#         ZeroDivisionError - деление на ноль.
#     AssertionError - выражение в функции assert ложно.
#     AttributeError - объект не имеет данного атрибута (значения или метода).
#     BufferError - операция, связанная с буфером, не может быть выполнена.
#     EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
#     ImportError - не удалось импортирование модуля или его атрибута.
#     LookupError - некорректный индекс или ключ.
#         IndexError - индекс не входит в диапазон элементов.
#         KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
#     MemoryError - недостаточно памяти.
#     NameError - не найдено переменной с таким именем.
#         UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
#     OSError - ошибка, связанная с системой.
#         BlockingIOError
#         ChildProcessError - неудача при операции с дочерним процессом.
#         ConnectionError - базовый класс для исключений, связанных с подключениями.
#             BrokenPipeError
#             ConnectionAbortedError
#             ConnectionRefusedError
#             ConnectionResetError
#         FileExistsError - попытка создания файла или директории, которая уже существует.
#         FileNotFoundError - файл или директория не существует.
#         InterruptedError - системный вызов прерван входящим сигналом.
#         IsADirectoryError - ожидался файл, но это директория.
#         NotADirectoryError - ожидалась директория, но это файл.
#         PermissionError - не хватает прав доступа.
#         ProcessLookupError - указанного процесса не существует.
#         TimeoutError - закончилось время ожидания.
#     ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
#     RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
#     NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
#     SyntaxError - синтаксическая ошибка.
#         IndentationError - неправильные отступы.
#             TabError - смешивание в отступах табуляции и пробелов.
#     SystemError - внутренняя ошибка.
#     TypeError - операция применена к объекту несоответствующего типа.
#     ValueError - функция получает аргумент правильного типа, но некорректного значения.
#     UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
#         UnicodeEncodeError - исключение, связанное с кодированием unicode.
#         UnicodeDecodeError - исключение, связанное с декодированием unicode.
#         UnicodeTranslateError - исключение, связанное с переводом unicode.
#
