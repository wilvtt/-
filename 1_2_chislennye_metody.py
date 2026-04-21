import math

#округление
def round_numbers(numbers, digits):
    return [round(x, digits) for x in numbers]

#погрешности
def calculate_errors(x):
    s = f"{x:.10f}".rstrip('0') # перевожу число в строку с 10ю знаками после запятой и убираю нолики

    if '.' in s:
        decimals = len(s.split('.')[1])
    else:
        decimals = 0   #считаем знаки после запятой

    last_digit = 10 ** (-decimals)  #точность записи числа
    absolute_error = last_digit / 2  #абсолютная погрешность
    relative_error = absolute_error / x if x != 0 else 0  #относительная

    return absolute_error, relative_error


#значащие цифры
def significant_figures(x):
    s = f"{x}".lower()

    if 'e' in s:
        s = f"{float(x):.10f}"

    s = s.strip().lstrip('0')  #убираю слева незначащие цифры

    if '.' in s:
        s = s.replace('.', '')

    s = s.rstrip('0') if '.' not in f"{x}" else s

    return len(s)

