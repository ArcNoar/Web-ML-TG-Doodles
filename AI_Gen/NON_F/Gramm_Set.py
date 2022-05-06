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
def model(ccpa):
    
    X_train, X_test, y_train, y_test = train_test_split(dataf,a_y,test_size=0.4,random_state=1508)
    #print(X_train, y_train)

    Construct_Grader = DecisionTreeClassifier(random_state=1508,ccp_alpha=ccpa)
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    #prediction = 'Нечего предсказывать'
    
    #w_data = np.array(word,dtype=np.float32)
    #prediction = Construct_Grader.predict(word)

    #Test_Pred = Construct_Grader.predict(data_test)
    #print(blyat)
    
    model_out = metrics.accuracy_score(y_test,y_pred)
    #print(model_out)

    
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
    #return str(prediction)
    #return round(normal_acc,2)
    

def alpha_trainer():
    lr = 0.00001
    best_ccp = 0.00625
    current_ccp = 0.00001
    best_acc = 1.3
    num_epoches = 1500
    


    for epoche in range(num_epoches):
        
        model_acc = model(current_ccp)
        if model_acc <= best_acc:
            current_ccp += lr
        else:
            best_ccp = current_ccp
            best_acc = model_acc

        if (epoche + 1) % 100 == 0:
            print(f'epoch {epoche + 1}/{num_epoches}, cur_alpha = {current_ccp} , best_alpha = {best_ccp}, Best_Acc = {best_acc}')
            

    return best_ccp

def show_alph():
    X_train, X_test, y_train, y_test = train_test_split(dataf,a_y,test_size=0.4,random_state=1508)
    #print(X_train, y_train)

    Construct_Grader = DecisionTreeClassifier(random_state=1508)
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    #prediction = 'Нечего предсказывать'
    
    #w_data = np.array(word,dtype=np.float32)
    #prediction = Construct_Grader.predict(word)

    #Test_Pred = Construct_Grader.predict(data_test)
    #print(blyat)
    
    model_out = metrics.accuracy_score(y_test,y_pred)
    #print(model_out)

    
    
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





        
def R_trainer():
    lr = 1
    best_r = 1
    current_r = 1
    best_acc = 1.3
    num_epoches = 3000
    


    for epoche in range(num_epoches):
        
        model_acc = model(current_r)
        if model_acc <= best_acc:
            current_r += lr
        else:
            best_r = current_r
            best_acc = model_acc

        if (epoche + 1) % 500 == 0:
            print(f'epoch {epoche + 1}/{num_epoches}, cur_r = {current_r} , best_r = {best_r}, Best_Acc = {best_acc}')
            show_alph(best_r)
            
    
    return best_r

    


def test_model(word):
    ccpa = 0.0009700000000000019
    X_train, X_test, y_train, y_test = train_test_split(dataf,a_y,test_size=0.4,random_state=1508)
    #print(X_train, y_train)

    Construct_Grader = DecisionTreeClassifier(random_state=1508,ccp_alpha=ccpa)
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    #prediction = 'Нечего предсказывать'
    
    #w_data = np.array(word,dtype=np.float32)
    prediction = Construct_Grader.predict(word)
    model_out = metrics.accuracy_score(y_test,y_pred)
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return str(prediction)


