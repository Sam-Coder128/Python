############################################################################################################################
#
# Program      : Retrain without SleepHours
# Functions    : compare_accuracy(), main()
# Input        : student_performance_ml.csv
# Output       : Accuracy before and after removing SleepHours
# Description  : Compares model accuracy with and without SleepHours feature.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def compare_accuracy(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    acc_full = accuracy_score(y_test, model.predict(X_test))

    X2 = df.drop(['FinalResult','SleepHours'], axis=1)
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y, test_size=0.2, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model2.fit(X_train2, y_train2)
    acc_reduced = accuracy_score(y_test2, model2.predict(X_test2))

    print("Accuracy with SleepHours:", acc_full)
    print("Accuracy without SleepHours:", acc_reduced)

def main():
    compare_accuracy("student_performance_ml.csv")

if __name__ == "__main__":
    main()
