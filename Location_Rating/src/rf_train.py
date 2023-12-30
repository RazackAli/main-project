



import csv
X=[]
y=[]
# opening the CSV file
i=0
with open('rating.csv', mode ='r')as file:

# reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        if i!=0:
            print(lines)
            r=[float(lines[0]),
               float(lines[1]),
               float(lines[2]),
               float(lines[3]),
               float(lines[4]),
               float(lines[5]),
               float(lines[6]),
               float(lines[7]),
               float(lines[8]),
               float(lines[9])]
            X.append(r)
            y.append(float(lines[10]))
        i=i+1

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators = 100)

clf.fit(X_train, y_train)

# Predict on dataset which model has not seen before
yp=clf.predict(X_test)

print(yp)
from sklearn.metrics import classification_report,confusion_matrix

print("\nconfusion_matrix\n",
          confusion_matrix(y_test, yp))
print("\nclassification_report\n",
          classification_report(y_test, yp))

import joblib

# Save the model as a pickle in a file
joblib.dump(clf, 'rf.pkl')

# Load the model from the file
knn_from_joblib = joblib.load('rf.pkl')

# Use the loaded model to make predictions
yp=knn_from_joblib.predict(X_test)



print("load model")

print("\nconfusion_matrix\n",
          confusion_matrix(y_test, yp))
print("\nclassification_report\n",
          classification_report(y_test, yp))