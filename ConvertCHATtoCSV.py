

# coding: utf-8

# In[1]:

import pandas as pd
import zipfile
import os

#CHAT2
data_xls = pd.read_excel('C:\DataExtracts\Book1.xlsx', header=1, index_col=0)
data_xls.to_csv('C:\DataExtracts\Book1.csv',sep='↑', encoding='utf-8')

print('winner winner chicken dinner')
