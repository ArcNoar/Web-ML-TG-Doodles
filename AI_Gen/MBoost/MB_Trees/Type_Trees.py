from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics

from AI_Gen.Data_Prep.MB_Data_Prep import X # General Tree X

# Type Y for trees
from AI_Gen.Data_Prep.MB_Data_Prep import Y_ADJECTIVE

from AI_Gen.Data_Prep.MB_Data_Prep import Y_DEPRICH

from AI_Gen.Data_Prep.MB_Data_Prep import Y_INTER

from AI_Gen.Data_Prep.MB_Data_Prep import Y_NAME

from AI_Gen.Data_Prep.MB_Data_Prep import Y_NOMIN

from AI_Gen.Data_Prep.MB_Data_Prep import Y_PREPOS

from AI_Gen.Data_Prep.MB_Data_Prep import Y_NOUN

from AI_Gen.Data_Prep.MB_Data_Prep import Y_NUMIN

from AI_Gen.Data_Prep.MB_Data_Prep import Y_PRICH

from AI_Gen.Data_Prep.MB_Data_Prep import Y_Verb

from AI_Gen.Data_Prep.MB_Data_Prep import Y_UNION

from AI_Gen.Data_Prep.MB_Data_Prep import Y_PTICK

from AI_Gen.Data_Prep.MB_Data_Prep import Y_STATE


def ADJ_Model(word=None,ccpa=0.0019300000000000044):
    
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_ADJECTIVE,test_size=0.4)
    
    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Deprich_Model(word=None,ccpa=0.000610000000000001):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_DEPRICH,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Inter_Model(word=None,ccpa=0.0007700000000000014):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_INTER,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Name_Model(word=None,ccpa=0.0005600000000000008):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_NAME,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Nomin_Model(word=None,ccpa=0.0010700000000000022):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_NOMIN,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Noun_Model(word=None,ccpa=0.0035400000000000084):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_NOUN,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Numin_Model(word=None,ccpa=0.0005400000000000008):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_NUMIN,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Prepos_Model(word=None,ccpa=0.0008600000000000016):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_PREPOS,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Prich_Model(word=None,ccpa=0.0005100000000000007):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_PRICH,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Ptick_Model(word=None,ccpa=0.000990000000000002):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_PTICK,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def State_Model(word=None,ccpa=0.0013100000000000028):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_STATE,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Union_Model(word=None,ccpa=0.000620000000000001):
  
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_UNION,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)

def Verb_Model(word=None,ccpa=0.0015400000000000034):
    
    X_train, X_test, y_train, y_test = train_test_split(X,Y_Verb,test_size=0.4)
    

    Construct_Grader = DecisionTreeClassifier()
    
    Construct_Grader = Construct_Grader.fit(X_train,y_train)
    
    y_pred = Construct_Grader.predict(X_test)
    if word is None:
        pass
    else:
        prediction = Construct_Grader.predict(word)
        print(prediction)
        return prediction
    model_out = metrics.accuracy_score(y_test,y_pred)
    
    normal_acc = model_out * 100
    
    print( f"Точность модели : { round(normal_acc,2)} %")
    return round(normal_acc,2)


model_list = {'ADJ' : ADJ_Model,
              'DEPRICH' : Deprich_Model,
              'Inter' : Inter_Model,
              'Name' : Name_Model,
              'Nomin' : Nomin_Model,
              'Noun' : Noun_Model,
              'Numin' : Numin_Model,
              'Prepos' : Prepos_Model,
              'Prich' : Prich_Model,
              'Ptick' : Ptick_Model,
              'State' : State_Model,
              'Union' : Union_Model,
              'Verb' : Verb_Model}