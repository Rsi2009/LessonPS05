# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5)  # массив из 5 случайных чисел
# print(random_array)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

random_array = np.random.rand(5)
plt.scatter(random_array, random_array)

print(random_array)

plt.xlabel("ось х")
plt.ylabel("ось y")
plt.title("Диаграмма рассеяния")
plt.show()