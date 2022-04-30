import collections
import csv
from re import split

import pandas as pd
import numpy as np

from random import randint

import matplotlib.pyplot as plt

#import rusyllab as rl

from ast import literal_eval







pd.set_option('display.max_rows', None) # Sets Unlimited columns to display
pd.set_option('display.max_columns', None) # Sets Unlimited columns to display
df = pd.read_csv("C:\\Users\\ArcNoar\\Desktop\\WORK\\Codeing\\ProjectCOde\\FREEZED\\AsiyaPROJ\\Sheesh\\Word_Data.csv")

"""
'ID' - 
'Слово' - 
'Длина'
'Количество слогов.'
'Слоги'
'Код Слогов' 
'Код'
'X_Cord' - 
'Y_Cord' - 
'SF' - 
'Категория' - 
'Тип' - 
"""
df_WT = df.loc[(df['Тип'] != 'NONE_T')]
df_Bad = df.loc[(df['Тип'] == 'NONE_T')]
print(df_Bad['Слово'])
#print(df_WT.head())
#parts = df_WT['Код Слогов']

X = df_WT.drop('ID',axis=1).copy() # Вырезаем ответ из данных.
X = X.drop('Тип',axis=1).copy()
X = X.drop('Категория',axis=1).copy()
X = X.drop('Слово',axis=1).copy()
X = X.drop('Слоги',axis=1).copy()
X = X.drop('X_Cord',axis=1).copy()
X = X.drop('Y_Cord',axis=1).copy()
X = X.drop('SF',axis=1).copy()
#X = X.drop('Код',axis=1).copy()


Normal_X = []
#print(X['Код'])
#print(len(X['Код']))

Test_Data = []

for i in range(0,657):
    if df['Тип'][i] != 'NONE_T':
        Data_I = []
        Data_I.append(literal_eval(df['Код'][i]))
        Data_I.append(int(df['Длина'][i]))
        Data_I.append(int(df['Количество слогов.'][i]))
        #Data_I.append(literal_eval(df['Код Слогов'][i]))


        Normal_X.append(Data_I)
    else:
        Data_I = []
        Data_I.append(literal_eval(df['Код'][i]))
        Data_I.append(int(df['Длина'][i]))
        Data_I.append(int(df['Количество слогов.'][i]))
        #Data_I.append(literal_eval(df['Код Слогов'][i]))


        Test_Data.append(Data_I)

#print(len(Test_Data))

#print(Normal_X[0])

y_pek = df_WT['Тип'].copy()

#print(y.unique())

Normal_Y = []
another_Y = []

"""
['NAME' 'VERB' 'STATE' 'NOUN' 'PTICK' 'UNION' 'PREPOS' 'NOMIN' 'ADJECTIVE'
 'INTER' 'DEPRICH' 'NUMIN']
"""

group_Keys = {
        'NAME' : 0,
        'VERB' : 1,
        'STATE' : 2,
        'NOUN' : 3,
        'PTICK' : 4,
        'UNION' : 5,
        'PREPOS' : 6,
        'NOMIN' : 7,
        'ADJECTIVE' : 8,
        'INTER' : 9,
        'DEPRICH' : 10,
        'NUMIN' : 11
}


for i in range(0,657):

    if df['Тип'][i] != 'NONE_T':
        another_Y.append(df['Тип'][i])
        Normal_Y.append(group_Keys[f"{df['Тип'][i]}"])
    else:
        pass

"""
[[15, 16, 11], 3, 1]
Code = [15, 16, 11] => 
Len = 3
P_A = 1

"""
y_df = pd.DataFrame(Normal_Y, columns = ['NAME' 'VERB' 'STATE' 'NOUN' 'PTICK' 'UNION' 'PREPOS' 'NOMIN' 'ADJECTIVE'
 'INTER' 'DEPRICH' 'NUMIN'])

# initialize list of lists
data = Normal_X

code = []
for i in data:
    code = i[0]
    
   
#code = [j for j in [i for i in data]]
#print(code)

pizdec = [] 
columba = ['Lenght','P_Amount']

def Pedoro(d):
    
    try:    
        for numba in range(40):
            
            pizdec.append(f'Code_{numba}')
    except Exception as _ex:
        print('ТЫ ДОЛБАЕБ')
            
def data_trans(data_b):
    collected_data = []
    
    for i in data_b:
        new_data = []
        for blyat in i:
            #print(blyat)
            if type(blyat) == list:
                for c in blyat:
                    #print(c)
                    #print('МЫ ТУТ')
                    new_data.append(c)
            else:
                #print(blyat)
                new_data.append(blyat)
        while len(new_data) < 42:
            new_data.append(0)
        collected_data.append(new_data)
        


    return collected_data

Pedoro(code)
#print(pizdec)
mega_columba = pizdec + columba
#print(pizdec + columba)

proc_data = data_trans(data)
test_pd = data_trans(Test_Data)
#print(mega_columba)

#print(proc_data)
# Create the pandas DataFrame
dataf = pd.DataFrame(proc_data, columns = mega_columba)
data_test = pd.DataFrame(test_pd, columns = mega_columba)
a_y = pd.DataFrame(another_Y,columns = ['Тип'])
#print(a_y)
#print(data_test.head())






