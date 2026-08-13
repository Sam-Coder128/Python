############################################################################################################################
#
# Program      : Train Decision Tree Model
# Functions    : train_model(), main()
# Input        : student_performance_ml.csv
# Output       : Trains Decision Tree model
# Description  : Imports DecisionTreeClassifier, creates model object, trains using fit().
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def train_model(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    print("Model trained successfully.")
    return model, X_test, y_test

def main():
    train_model("student_performance_ml.csv")

if __name__ == "__main__":
    main()
