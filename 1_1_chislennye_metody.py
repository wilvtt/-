import numpy as np

data = np.array([4.8, 5.0, 4.9, 4.8, 5.0])  #список чисел превращаю в массив

mean = np.mean(data)   #среднее значение
std = np.std(data, ddof=1)   #np.std - считает среднее, складывает, делит на n-1, берет корень. ddof=1 чтобы делилось не на n а на n-1
error = std / np.sqrt(len(data)) #std - разброс, (len(data)) - кол-во измерений

print("Среднее:", round(mean, 2))
print("Стандартное отклонение:", round(std, 3))
print("Погрешность среднего:", round(error, 3))