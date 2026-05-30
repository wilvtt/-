from math import sin

eps = 1e-5  #нужная точность
x = 1.1   #начальное приближение(когда выяснила в тетради, что х между 1 и 1.2)

while True:
    xn = 1 / sin(x)   #сама формула

    if abs(xn - x) < eps:  #сравнение с точностью
        break

    x = xn

print("Корень =", xn)