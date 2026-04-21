def solve_task_1():
    beta, t = 2, 2  #beta - двоичная система, t - цифры в мантиссе
    p_range = range(-1, 2)  # возможные степени
    numbers = {0.0}

    for d1 in range(1, beta):  #генерация мантиссы, чтобы первая цифра не была нулем(нормализация)
        for d2 in range(beta):
            mantissa = d1 * (beta ** -1) + d2 * (beta ** -2)
            for p in p_range:
                val = mantissa * (beta ** p)    #умножаем на степень
                numbers.add(val)    #учитываем и + и -
                numbers.add(-val)

    sorted_nums = sorted(list(numbers))
    print(f"Задача 1: Количество чисел = {len(sorted_nums)}")
    print(f"Числа: {sorted_nums}")


def solve_task_2():
    beta, t = 10, 3
    p1, p2 = -9, 9

    u_level = 1 * (beta ** (p1 - 1))  # самое маленькое нормализованное число
    o_level = (1 - beta ** -t) * (beta ** p2)  #самое юольшое

    print(f"\nЗадача 2:")
    print(f"Нижняя граница (min pos): {u_level:.1e}")
    print(f"Верхняя граница (max): {o_level}")


solve_task_1()
solve_task_2()