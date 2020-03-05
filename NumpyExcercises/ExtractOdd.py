import numpy as np

value = np.random.randint(0,100, 10)
print(value)

condition = value %2 == 0
print(condition)

print(value[condition])