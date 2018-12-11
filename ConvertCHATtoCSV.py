

# coding: utf-8

# In[1]:

import pandas as pd
import zipfile
import os

#CHAT2
data_xls = pd.read_excel('C:\DataExtracts\SprintFiles\CHAT2.xlsx', header=1, index_col=0)
data_xls.to_csv('C:\DataExtracts\SprintFiles\CHAT2.csv',sep='↑', encoding='utf-8')

#CHAT
#data_xls = pd.read_excel('C:\DataExtracts\SprintFiles\CHAT.xlsx', header=1, index_col=0)
#data_xls.to_csv('C:\DataExtracts\SprintFiles\CHAT.csv',sep='↑', encoding='utf-8')

#Remove Non-printables
def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)

#EOF
#os.system("C:\\Users\\s_powerbi\\Desktop\\vbsScripts\\ConvertEOFtoxlsx.vbs")
#data_xls = pd.read_excel('C:\DataExtracts\SprintFiles\EOF.xlsx', index_col=0, usecols= [0,2,3,4,5,6,7,8,9,10,11,13,14,24,28,29])

#data_xls['WO Notes New'] = data_xls['WO Notes New'].apply(remove_non_ascii)

#data_xls.to_csv('C:\DataExtracts\SprintFiles\EOF.csv',sep='¡', encoding='utf-8')

print('winner winner chicken dinner')
