############################################################################################################################
#
# Program      : Train with StudyHours and Attendance only
# Functions    : train_subset(), main()
# Input        : student_performance_ml.csv
# Output       : Accuracy with subset features vs full features
# Description  : Compares accuracy using only StudyHours and Attendance.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_subset(filename):
    df = pd.read_csv(filename)
    X_full = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X_full, y, test_size=0.2, random_state=42)
    model_full = DecisionTreeClassifier(random_state=42)
    model_full.fit(X_train, y_train)
    acc_full = accuracy_score(y_test, model_full.predict(X_test))

    X_sub = df[['StudyHours','Attendance']]
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X_sub, y, test_size=0.2, random_state=42)
    model_sub = DecisionTreeClassifier(random_state=42)
    model_sub.fit(X_train2, y_train2)
    acc_sub = accuracy_score(y_test2, model_sub.predict(X_test2))

    print("Full feature accuracy:", acc_full)
    print("Subset feature accuracy:", acc_sub)

def main():
    train_subset("student_performance_ml.csv")

if __name__ == "__main__":
    main()
