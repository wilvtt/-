import math

def f(x):
    if x <= 0:
        return None  #логарифм не определён
    return math.log10(x) + 6 - x ** 2 #функция

#параметры поиска
x_start = 0.1
x_end = 4.0
step = 0.1

#список для хранения интервалов с корнями
intervals = []

#предыдущее значение функции
x_prev = x_start
f_prev = f(x_prev)

#прохожу по сетке
x_current = x_start + step
while x_current <= x_end:
    f_current = f(x_current)

    #смена знака
    if f_prev * f_current < 0:
        # Знаки разные — корень между x_prev и x_current
        intervals.append((x_prev, x_current))
        print(f"Корень в интервале ({x_prev:.2f}, {x_current:.2f})")

    x_prev = x_current
    f_prev = f_current
    x_current += step

print(f"\nВсего интервалов: {len(intervals)}")