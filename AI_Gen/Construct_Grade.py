
from sklearn.tree import DecisionTreeClassifier


from sklearn.model_selection import train_test_split


from AI_Gen.CG_Data_Prep import X, y




X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=20)


Construct_Grader = DecisionTreeClassifier(random_state=20)

Construct_Grader = Construct_Grader.fit(X_train,y_train)
