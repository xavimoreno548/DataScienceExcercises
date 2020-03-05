import pandas as pd
import numpy as np

serie_one = pd.Series(list('abcd'))
serie_two = pd.Series(np.arange(4))

df = pd.DataFrame({'col_1':serie_one, 'col_2':serie_two})
print(df)