import math

#функция
def f(x):
    return x * math.sin(x) - 1

#изначальный отрезок
a = 1
b = 2
#точность
eps = 1e-4

#итерация
while (b - a) / 2 > eps:
    c = (a + b) / 2  #середина отрезка
    if f(a) * f(c) <= 0:
        b = c
    else:
        a = c

x = (a + b) / 2

print("Корень:", round(x, 6))
print("Погрешность:", (b - a) / 2)