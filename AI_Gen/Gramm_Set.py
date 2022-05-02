#from os import name
from AI_Gen.Data_Prep.Gramma_Data_Prep import dataf ,a_y, data_test #, y_pek,y_df

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import cross_val_score


from sklearn import metrics
#from sklearn.model_selection import train_test_split


#X, y = np.array(dataf, dtype=np.float32),np.array(y_df, dtype=np.float32)

# 0) Prepare data
def model(ccpa,train_set=[],word='None',test=None):
    
    X_train, X_test, y_train, y_test = train_test_split(dataf,a_y,test_size=0.3,random_state=100)
    #print(X_train, y_train)

    Construct_Grader = DecisionTreeClassifier(random_state=100,ccp_alpha=ccpa)
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    #prediction = 'Нечего предсказывать'
    
    #w_data = np.array(word,dtype=np.float32)
    #prediction = Construct_Grader.predict(word)
    if test == 0:
        big_pred = Construct_Grader.predict(train_set)
    elif test == 1:
        prediction = Construct_Grader.predict(word)

    #Test_Pred = Construct_Grader.predict(data_test)
    #print(blyat)
    
    model_out = metrics.accuracy_score(y_test,y_pred)
    #print(model_out)
    # Визуализируем дерево.
    plt.figure(figsize=(250,125),constrained_layout=True)
    plot_tree(Construct_Grader,
              filled=True,
              rounded=True,
              proportion=True,
              max_depth=5
              )
    plt.show()

    """
    path = Construct_Grader.cost_complexity_pruning_path(X_train, y_train) # Determine values for alpha
    ccp_alphas = path.ccp_alphas # Extract different for alpha
    ccp_alphas = ccp_alphas[:-1] # Exclude the maximum alpha
    
    clf_dts = [] # Container for decision trees.
    
    # now create one decision tree per value for alpha and store it in the array
    for ccp_alpha in ccp_alphas:
        Construct_Grader = DecisionTreeClassifier(random_state=0,ccp_alpha=ccp_alpha)
        Construct_Grader.fit(X_train,y_train)
        clf_dts.append(Construct_Grader)
    
    # Теперь изобразим графиком эффективность деревьев
    train_scores = [Construct_Grader.score(X_train, y_train) for Construct_Grader in clf_dts]
    test_scores = [Construct_Grader.score(X_test,y_test) for Construct_Grader in clf_dts]
    fig, ax = plt.subplots()
    ax.set_xlabel("alpha")
    ax.set_ylabel("accuracy")
    ax.set_title("Accuracy vs alpha for training and testing sets")
    ax.plot(ccp_alphas,train_scores,marker='o',label="train",drawstyle="steps-post")
    ax.plot(ccp_alphas,test_scores,marker='o',label="test",drawstyle="steps-post")
    ax.legend()
    plt.show()
    """
    
    normal_acc = model_out * 100
    
    #return f"Точность модели : { round(normal_acc,2)} %"
    if test == 0:
        return big_pred
    elif test == 1:
        return str(prediction)
    else:
        return round(normal_acc,2)
    

def alpha_trainer(type=None,aword='None'):
    lr = 0.000001
    best_ccp = 0.00625
    current_ccp = 0.000001
    best_acc = 37.88
    num_epoches = 1000
    if type == 0:
        test_predict =  model(best_ccp,data_test,test=type)
        print('Ответы на Данные.')
        print(test_predict)
        return str(best_ccp)
    elif type == 1:
        test_02 = model(0.0006260000000000087,word=aword,test=type)
        return test_02


    for epoche in range(num_epoches):
        
        model_acc = model(current_ccp)
        if model_acc <= best_acc:
            current_ccp += lr
        else:
            best_ccp = current_ccp
            best_acc = model_acc

        if (epoche + 1) % 100 == 0:
            print(f'epoch {epoche + 1}/{num_epoches}, cur_alpha = {current_ccp} , best_alpha = {best_ccp}, Best_Acc = {best_acc}')
            


        


"""
Оно работает!!!
Не идеально. 
НО РАБОТАЕТ!!!
"""