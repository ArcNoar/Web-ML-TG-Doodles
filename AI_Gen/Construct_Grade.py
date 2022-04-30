
from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics
from sklearn.model_selection import train_test_split


from AI_Gen.Gramma_Data_Prep import X,y




X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=20)


Construct_Grader = DecisionTreeClassifier(random_state=20)

Construct_Grader = Construct_Grader.fit(X_train,y_train)

y_pred = Construct_Grader.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test,y_pred))



#print(Construct_Grader.predict(Test_Data[0]))