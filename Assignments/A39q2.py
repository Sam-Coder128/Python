############################################################################################################################
#
# Program      : Predict Results for X_test
# Functions    : predict_results(), main()
# Input        : student_performance_ml.csv
# Output       : Displays predicted values and actual values
# Description  : Uses trained model to predict results for X_test.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def predict_results(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Predicted:", y_pred)
    print("Actual:", y_test.values)

def main():
    predict_results("student_performance_ml.csv")

if __name__ == "__main__":
    main()
