############################################################################################################################
#
# Program      : Identify Misclassified Students
# Functions    : misclassified(), main()
# Input        : student_performance_ml.csv
# Output       : Rows where y_test != y_pred
# Description  : Displays misclassified students and counts them.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def misclassified(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mismatches = X_test[y_test != y_pred]
    print("Misclassified rows:\n", mismatches)
    print("Count of misclassified:", len(mismatches))

def main():
    misclassified("student_performance_ml.csv")

if __name__ == "__main__":
    main()
