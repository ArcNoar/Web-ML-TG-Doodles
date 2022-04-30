"""
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics

from sklearn.model_selection import train_test_split


from sklearn.svm import SVC



from AI_Gen.CG_Data_Prep import X, y

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4)




svc = SVC(probability=True,kernel='linear')

abc = AdaBoostClassifier(n_estimators=40,base_estimator=svc,learning_rate=0.01)

Construct_AB_Grader = abc.fit(X_train, y_train)

y_pred = Construct_AB_Grader.predict(X_test)

#print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
"""