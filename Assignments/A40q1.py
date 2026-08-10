############################################################################################################################
#
# Program      : Feature Importance in Decision Tree
# Functions    : train_model(), main()
# Input        : student_performance_ml.csv
# Output       : Importance scores of each feature
# Description  : Trains Decision Tree and displays feature importances.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def train_model(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    for col, score in zip(X.columns, model.feature_importances_):
        print(col, ":", score)
    print("Most important:", X.columns[model.feature_importances_.argmax()])
    print("Least important:", X.columns[model.feature_importances_.argmin()])

def main():
    train_model("student_performance_ml.csv")

if __name__ == "__main__":
    main()
