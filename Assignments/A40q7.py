############################################################################################################################
#
# Program      : Compare Random States
# Functions    : compare_random_states(), main()
# Input        : student_performance_ml.csv
# Output       : Testing accuracy for random_state=0,10,42
# Description  : Trains Decision Tree with different random states and compares accuracy.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def compare_random_states(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    for state in [0,10,42]:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=state)
        model = DecisionTreeClassifier(random_state=state)
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test)) * 100
        print("Testing Accuracy with random_state =", state, ":", acc, "%")

def main():
    compare_random_states("student_performance_ml.csv")

if __name__ == "__main__":
    main()
