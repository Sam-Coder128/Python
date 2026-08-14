############################################################################################################################
#
# Program      : Training vs Testing Accuracy
# Functions    : compare_accuracy(), main()
# Input        : student_performance_ml.csv
# Output       : Displays training and testing accuracy
# Description  : Compares training and testing accuracy to check overfitting/underfitting.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def compare_accuracy(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train)) * 100
    test_acc = accuracy_score(y_test, model.predict(X_test)) * 100
    print("Training Accuracy:", train_acc, "%")
    print("Testing Accuracy:", test_acc, "%")
    if train_acc > 95 and test_acc < train_acc:
        print("Model may be overfitting.")
    else:
        print("Model is generalizing well.")

def main():
    compare_accuracy("student_performance_ml.csv")

if __name__ == "__main__":
    main()
