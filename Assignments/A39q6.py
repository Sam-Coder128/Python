############################################################################################################################
#
# Program      : Compare max_depth Values
# Functions    : compare_depths(), main()
# Input        : student_performance_ml.csv
# Output       : Testing accuracy for max_depth=1,3,None
# Description  : Trains three models with different max_depth and compares accuracy.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def compare_depths(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    for depth in [1,3,None]:
        model = DecisionTreeClassifier(max_depth=depth, random_state=42)
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test)) * 100
        print("Testing Accuracy with max_depth =", depth, ":", acc, "%")

def main():
    compare_depths("student_performance_ml.csv")

if __name__ == "__main__":
    main()
