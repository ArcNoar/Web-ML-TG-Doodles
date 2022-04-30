from os import name
from AI_Gen.Gramma_Data_Prep import dataf ,a_y, data_test #, y_pek,y_df

#import torch
#import torch.nn as nn
#import numpy as np
#from sklearn import datasets
#from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics
#from sklearn.model_selection import train_test_split


#X, y = np.array(dataf, dtype=np.float32),np.array(y_df, dtype=np.float32)

# 0) Prepare data
def model():
    
    X_train, X_test, y_train, y_test = train_test_split(dataf,a_y,random_state=20)


    Construct_Grader = DecisionTreeClassifier(random_state=20)
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)

    #Test_Pred = Construct_Grader.predict(data_test)
    #print(blyat)
    
    print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
   


if __name__ == '__main__':
    model()


"""
Оно работает!!!
Не идеально. 
НО РАБОТАЕТ!!!
"""