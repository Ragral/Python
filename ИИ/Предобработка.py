import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])
#Бинаризация данных(преобразование числовых значений в булевые)
data_binarized = preprocessing.Binarizer(threshold = 2.1).transform(input_data)
print("\nБинаризация данных\n", data_binarized)

#Исключение среднего
print("\nBefore:")
print("Среднее значение = ", input_data.mean(axis = 0))
print("Стандартное отклонение = ", input_data.std(axis = 0))
data_scala = preprocessing.scale(input_data)
print("\nAfter:")
print("Среднее значение = ", data_scala.mean(axis = 0))
print("Стандартное отклонение = ", data_scala.std(axis = 0))

#Масштабирование
data_scala_minmax = preprocessing.MinMaxScaler(feature_range = (0, 1))
data_scala_minmax = data_scala_minmax.fit_transform(input_data)
print("\nМин и макс масштабирования\n", data_scala_minmax)

#Нормализация данных
data_normalized_l1 = preprocessing.normalize(input_data, norm = "l1")
data_normalized_l2 = preprocessing.normalize(input_data, norm = "l2")
print("\nНормализация методом наименьшего обсолютного отклонения\n", data_normalized_l1)
print("\nНормализация методом наименьших квадратов\n",data_normalized_l2)