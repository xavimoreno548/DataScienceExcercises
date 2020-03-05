import numpy as np

value_array = np.random.randint(0, 100, 20)
print(value_array)
print(np.where(value_array %2 == 0, value_array, -1))