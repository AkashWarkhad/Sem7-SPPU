# contact@mitu.co.in

# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing Dataset
data_set = pd.read_csv('201805-capitalbikeshare-tripdata.csv')

# Data set summary
print(data_set.info())

# Separation of IV, DV
X = data_set.iloc[:, [0, 3, 5]].values
y = data_set.iloc[:, -1].values
print(X[:5])
print(y[:5])

# y has Categorical data hence needs Encoding
from sklearn.preprocessing import LabelEncoder
labelencoder_y =LabelEncoder()
y = labelencoder_y.fit_transform(y)
print("Sample y:",y[:5])
print("0 :",labelencoder_y.classes_[0])
print("1 :",labelencoder_y.classes_[1])

# Splitting of Data into Training & Testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Machine: Classifier | Classifier: Decision Tree
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=4, random_state=0)
classifier.fit(X_train, y_train)

# criterion = entropy
# [[15955  9342]
#  [10429 57803]]

# citerion = gini
# [[16997  8300]
#  [12583 55649]]

# criterion = entropy, min_sample_leaf = 2
# [[16965  8332]
#  [12405 55827]]

# criterion = entropy, min_sample_leaf = 3
# [[16016  9281]
#  [ 9984 58248]]

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
