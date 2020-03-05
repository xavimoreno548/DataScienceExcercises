import pandas as pd
import numpy as np

my_list = list('abcd')
my_array = np.arange(4)
my_serie = pd.Series(dict(zip(my_list, my_array)))

print(my_serie.to_frame().reset_index())