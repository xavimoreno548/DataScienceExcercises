import pandas as pd
import numpy as np

mylist = list('abcd')
myarray = np.arange(4)
mydict = dict(zip(mylist, myarray))

list_serie = pd.Series(mylist)
array_serie = pd.Series(myarray)
dict_serie = pd.Series(mydict)

print(list_serie)
print(array_serie)
print(dict_serie)