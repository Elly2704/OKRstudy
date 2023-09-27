# Конструкция под названием match/case, которая позволяет достаточно гибко анализировать переменные на соответствие
# шаблонов и для найденного совпадения выполнять некоторые заданные операции. Данный оператор имеет следующий синтаксис:
match <переменная>:
    case <шаблон_1>:
        операторы
    ...
    case < шаблон_n>:
        операторы
    case _:
        иначе (default)

method = 'post'
match method:
    case "post":
        print("POST-запрос")
    case "get":
        print("GET-запрос")
    case _:
        print("Неподдерживаемый тип запроса")

def get_data(value):
    match value:
        case int():
            return value
        case float():
            return value
        case str():
            return value

    return None