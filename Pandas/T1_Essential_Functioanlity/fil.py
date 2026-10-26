import numpy as np
import pandas as pd

def fil(x):
    if x>10:
        return x
    return 

li=[15,6,7,8,9,12,22,33]
li2=[]

print(list(filter(fil,li)))
print([x for x in li if x > 10])
