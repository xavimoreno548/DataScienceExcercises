import numpy as np

value = np.random.randint(0, 20, 10)

odd_value = np.where(value %2 == 0, value, -1)

print(odd_value)
print(value)