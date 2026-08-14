############################################################################################################################
#
# Program      : Calculate Model Accuracy
# Functions    : calculate_accuracy(), main()
# Input        : student_performance_ml.csv
# Output       : Displays accuracy in percentage
# Description  : Uses accuracy_score to calculate model accuracy.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def calculate_accuracy(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred) * 100
    print("Model Accuracy:", acc, "%")

def main():
    calculate_accuracy("student_performance_ml.csv")

if __name__ == "__main__":
    main()
