
import csv
from re import split

import pandas as pd
import numpy as np

from random import randint
import matplotlib.pyplot as plt

#import rusyllab as rl

from ast import literal_eval

#from sklearn.model_selection import train_test_split

#from sklearn.tree import DecisionTreeClassifier

#from sklearn import metrics
#from sklearn.ensemble import GradientBoostingClassifier

#from sklearn.metrics import confusion_matrix
#from sklearn.metrics import plot_confusion_matrix






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

df_WT = df.loc[(df['Тип'] != 'NONE_T')] # Классифицированные Данные
df_Bad = df.loc[(df['Тип'] == 'NONE_T')] # Неклассифицированные Данные

y_all = df_WT['Тип'].copy() # Стандартный Датафрейм из ответами на классифицированные данные.

#print(df_WT['Тип'].unique())
"""
1.NAME
2.VERB
3.STATE
4.NOUN
5.PTICK
6.UNION
7.PREPOS
8.NOMIN
9.ADJECTIVE
10.INTER
11.DEPRICH
12.PUNCTATION
13.SYMBOL
14.NUM
15.NUMIN
16.PRICH
"""
DF_VERB = df.loc[(df['Тип'] == 'VERB')] # 1021
"""
DF_NAME = df.loc[(df['Тип'] == 'NAME')] # 31
DF_STATE = df.loc[(df['Тип'] == 'STATE')] # 235
DF_NOUN = df.loc[(df['Тип'] == 'NOUN')] # 835
DF_PTICK = df.loc[(df['Тип'] == 'PTICK')] # 16
DF_UNION = df.loc[(df['Тип'] == 'UNION')] # 30
DF_PREPOS = df.loc[(df['Тип'] == 'PREPOS')] # 30
DF_NOMIN = df.loc[(df['Тип'] == 'NOMIN')] # 171
DF_ADJ = df.loc[(df['Тип'] == 'ADJECTIVE')] # 337
DF_INTER = df.loc[(df['Тип'] == 'INTER')] # 18
DF_DEPRICH = df.loc[(df['Тип'] == 'DEPRICH')] # 75
DF_PUNCT = df.loc[(df['Тип'] == 'PUNCTATION')] # 1
DF_SYMBOL = df.loc[(df['Тип'] == 'SYMBOL')] # 1
DF_NUM = df.loc[(df['Тип'] == 'NUM')] # 9
DF_NUMIN = df.loc[(df['Тип'] == 'NUMIN')] # 25
DF_PRICH = df.loc[(df['Тип'] == 'PRICH')] # 22
"""

print(len(DF_VERB))
"""
print(len(DF_NAME))
print(len(DF_STATE))
print(len(DF_NOUN))
print(len(DF_PTICK))
print(len(DF_UNION))
print(len(DF_PREPOS))
print(len(DF_NOMIN))
print(len(DF_ADJ))
print(len(DF_INTER))
print(len(DF_DEPRICH))
print(len(DF_PUNCT))
print(len(DF_SYMBOL))
print(len(DF_NUM))
print(len(DF_NUMIN))
print(len(DF_PRICH))
"""


def X_Get(DF):
    def data_puller(frame,max_len=len(df)):
        Normalized_Frame = []
        for i in range(0,max_len):
            
            try:
                Data_I = []
                Data_I.append(frame['Длина'][i])
                Data_I.append(frame['Количество слогов.'][i])
                Data_I.append(literal_eval(frame['Код Слогов'][i]))
                Data_I.append(literal_eval(frame['Код'][i]))
    
                Normalized_Frame.append(Data_I)
            except Exception as _ex:
                pass
    
        return Normalized_Frame
    
    def Normal_DF(Normal_Data):
        data = Normal_Data
          
        #Get Ending (Last Part) 
        for i in data:
            w_part = i[2][len(i[2]) - 1]
            #print(len(w_part))
            joined_part = int(''.join([str(i) for i in w_part]))
            i[2] = round(np.log(joined_part),3)
         
            
    
        
        
        def Column_Create():
            Columns = []
            try:    
                for w_index in range(35):
                    
                    Columns.append(f'Code_{w_index}')
            except Exception as _ex:
                print('Something Wrong : ',_ex)
                 
                
            return Columns
    
        def data_trans(data_b):
            
            collected_data = []
            
            for i in data_b:
                new_data = []
                for info in i:
                    
                    if type(info) == list:
                        for c in info:
                            
                            new_data.append(c)
                    else:
                        
                        new_data.append(info)
                #while len(new_data) < 38:
                #    pass
                collected_data.append(new_data)
                
    
    
            return collected_data
        
        Code_Columns = Column_Create()
        Additional_Col = ['Lenght','P_Amount','Ending']
        
        DF_Columns = Additional_Col + Code_Columns 
        proc_data = data_trans(data)
        
        # Create the pandas DataFrame
        #dataf = pd.DataFrame(proc_data, columns = DF_Columns) # X_DF
        dataf = 0
    
        #print(dataf.head())
        return dataf, proc_data

    Normal = data_puller(DF)
    Output = Normal_DF(Normal)
    X = Output[0]
    GX = Output[1]

    return X,GX


def Y_Get(w_type,max_len=len(df)):
    global y_all
    
    #print(current_df)
    Normal_Y = []
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
            'NUMIN' : 11,
            'PUNCTATION' : 12,
            'PRICH' : 13,
            'SYMBOL' : 14,
            'NUM' : 15
    }

    for i in y_all:
        if i != w_type:
            Normal_Y.append(0)
        else:
            Normal_Y.append(1)

    NDF_Y = pd.DataFrame(Normal_Y,columns = ['Тип'])

    return NDF_Y, Normal_Y
        


#TEST Proc
X_T = X_Get(df_Bad)[0]
#print(X_T)

#BASE_X
X = X_Get(df_WT)[0]
#print(X.head())

#BASE_Y
#print(y_all.head())

#Verb Proc
Y_Verb = Y_Get('VERB')[0]
#print(Y_Verb.head())

#print(len(Y_Verb))
#print(len(X)) #1021
#print(len(X_Verb['Ending'].unique()))# 197
#print(X_Verb['Ending'].unique())

#Noun Proc
Y_NOUN = Y_Get('NOUN')[0]
#print(Y_NOUN.head())
#print(Y_NOUN)
#print(len(X_NOUN)) #1021
#print(len(X_NOUN['Ending'].unique()))# 197
#print(X_NOUN['Ending'].unique())


#NAME Proc
Y_NAME = Y_Get('NAME')[0]


#PTICK Proc
Y_PTICK = Y_Get('PTICK')[0]

#UNION Proc
Y_UNION = Y_Get('UNION')[0]

#PREPOS Proc
Y_PREPOS = Y_Get('PREPOS')[0]

#NOMIN Proc
Y_NOMIN = Y_Get('NOMIN')[0]

#ADJECTIVE
Y_ADJECTIVE = Y_Get('ADJECTIVE')[0]

#INTER Proc
Y_INTER = Y_Get('INTER')[0]

#DEPRICH Proc
Y_DEPRICH = Y_Get('DEPRICH')[0]

#PUNCT PROC
#Y_PUNCTATION = Y_Get('PUNCTATION')

#STATE Proc
Y_STATE = Y_Get('STATE')[0]

#SYMBOL Proc
#Y_SYMBOL = Y_Get('SYMBOL')

#NUM Proc
#Y_NUM = Y_Get('NUM')

#NUMIN Proc
Y_NUMIN = Y_Get('NUMIN')[0]

#PRICH Proc
Y_PRICH = Y_Get('PRICH')[0]



# Grad Prepare 
GX_Base = X_Get(df_WT)[1]


GY_Verb = Y_Get('VERB')[1]

GY_Noun = Y_Get('NOUN')[1]
#print(GY_Noun)

#NAME Proc
GY_Name = Y_Get('NAME')[1]


#PTICK Proc
GY_Ptick = Y_Get('PTICK')[1]

#UNION Proc
GY_Union = Y_Get('UNION')[1]

#PREPOS Proc
GY_Prepos = Y_Get('PREPOS')[1]

#NOMIN Proc
GY_Nomin = Y_Get('NOMIN')[1]

#ADJECTIVE
GY_Adjective = Y_Get('ADJECTIVE')[1]

#INTER Proc
GY_Inter = Y_Get('INTER')[1]

#DEPRICH Proc
GY_Deprich = Y_Get('DEPRICH')[1]


#STATE Proc
GY_State = Y_Get('STATE')[1]


#NUMIN Proc
GY_Numin = Y_Get('NUMIN')[1]

#PRICH Proc
GY_Prich = Y_Get('PRICH')[1]
