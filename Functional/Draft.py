from sklearn.datasets import make_classification
import numpy as np
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=1)

Myx = np.array([18,9,10,123923])
Myx_List = [18,9,10,123923]
#print(X)
print(Myx)
print(Myx_List)

print(y)