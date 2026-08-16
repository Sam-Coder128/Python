############################################################################################################################
#
# Program      : Train with max_depth=None
# Functions    : train_and_compare(), main()
# Input        : student_performance_ml.csv
# Output       : Training and Testing accuracy
# Description  : Trains Decision Tree with max_depth=None and compares accuracies.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_and_compare(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train)) * 100
    test_acc = accuracy_score(y_test, model.predict(X_test)) * 100
    print("Training Accuracy:", train_acc, "%")
    print("Testing Accuracy:", test_acc, "%")
    if train_acc == 100 and test_acc < train_acc:
        print("Overfitting: Model memorized training data but generalizes poorly.")

def main():
    train_and_compare("student_performance_ml.csv")

if __name__ == "__main__":
    main()
