############################################################################################################################
#
# Program      : Manual Accuracy Calculation
# Functions    : manual_accuracy(), main()
# Input        : student_performance_ml.csv
# Output       : Manual accuracy vs sklearn accuracy
# Description  : Calculates accuracy manually and compares with sklearn.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def manual_accuracy(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    correct = sum(y_test.values == y_pred)
    manual_acc = correct / len(y_test)
    sklearn_acc = accuracy_score(y_test, y_pred)

    print("Manual accuracy:", manual_acc)
    print("Sklearn accuracy:", sklearn_acc)

def main():
    manual_accuracy("student_performance_ml.csv")

if __name__ == "__main__":
    main()
