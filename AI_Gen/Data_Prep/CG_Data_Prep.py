
import csv

import pandas as pd
import numpy as np

from random import randint

import matplotlib.pyplot as plt





pd.set_option('display.max_rows', None) # Sets Unlimited columns to display
df = pd.read_csv("C:\\Users\\ArcNoar\\Desktop\\WORK\\Codeing\\ProjectCOde\\FREEZED\\AsiyaPROJ\\Sheesh\\All_Sent.csv")
#df = pd.read_csv("C:\\Users\\ArcNoar\\Desktop\\WORK\\Codeing\\ProjectCOde\\FREEZED\\AsiyaPROJ\\Sheesh\\Pred_S.csv")

df.columns = ['Sentence',
              'Order_Val',
              'X_Сord',
              'Y_Cord',
              'Grade',
              'TR']




#DFA_Success = df.loc[(df['TR'] == 'SUCCESS')]
#DFA_FAIL = df.loc[(df['TR'] == 'FAIL')]

#print(DFA_FAIL['X_Сord'])
#print(DFA_Success)
"""
plt.scatter(DFA_FAIL['X_Сord'],DFA_FAIL['Y_Cord'],color='red',label='FAIL')
plt.scatter(DFA_Success['X_Сord'],DFA_Success['Y_Cord'],color='green',label='SUCCESS')

plt.legend()
plt.show()
"""


X = df.drop('Grade',axis=1).copy() # Вырезаем ответ из данных.
X = X.drop('Sentence',axis=1).copy()
X = X.drop('TR',axis=1).copy()
#print(X)
#print(X.dtypes)

y = df['Grade'].copy()



"""
def Test_X(order_v,X_Cord,Y_Cord):


    X_Data = [[order_v,X_Cord,Y_Cord]]

    Test = pd.DataFrame(X_Data, columns = ['Order_Val', 'X_Сord','Y_Cord'])

    return Test
"""
