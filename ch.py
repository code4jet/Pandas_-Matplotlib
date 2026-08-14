# name='n2'
# key='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'
# link='https://build.nvidia.com/settings/api-keys'

import os
import pandas as pd

# print(os.path.exists("examples/fdic_failed_bank_list.html"))

x=pd.Series([1,2,3])
y=pd.Series([3,3,3])
print(x.corr(y))
