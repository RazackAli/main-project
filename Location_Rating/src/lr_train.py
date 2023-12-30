



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
            r=[int(lines[0]),
               int(lines[1]),
               int(lines[2]),
               int(lines[3]),
               int(lines[4]),
               int(lines[5]),
               int(lines[6]),
               int(lines[7]),
               int(lines[8]),
               int(lines[9])]
            X.append(r)
            y.append(int(lines[10]))
        i=i+1

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

regr = LinearRegression()

regr.fit(X_train, y_train)

# Predict on dataset which model has not seen before
yp=regr.predict(X_test)

print(yp)
from sklearn.metrics import classification_report,confusion_matrix

# print("\nconfusion_matrix\n",
#           confusion_matrix(y_test, yp))
# print("\nclassification_report\n",
#           classification_report(y_test, yp))
#
# import joblib
#
# # Save the model as a pickle in a file
# joblib.dump(regr, 'lr.pkl')
#
# # Load the model from the file
# lr = joblib.load('lr.pkl')
#
# # Use the loaded model to make predictions
# yp=lr.predict(X_test)
#
#
#
# print("load model")
# print("\nconfusion_matrix\n",
#           confusion_matrix(y_test, yp))
# print("\nclassification_report\n",
#           classification_report(y_test, yp))



from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y_true=y_test, y_pred=yp)
# squared True returns MSE value, False returns RMSE value.
mse = mean_squared_error(y_true=y_test, y_pred=yp)  # default=True
rmse = mean_squared_error(y_true=y_test, y_pred=yp, squared=False)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)