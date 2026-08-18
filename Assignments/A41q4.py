############################################################################################################################
#
# Program      : Wine Dataset - Step 1,2,3,4 (Get + Prepare + Train + Test)
# Functions    : get_data(), prepare_data(), train_model(), test_model(), main()
# Input        : Wine dataset
# Output       : Predictions on test data
# Description  : Loads, prepares, trains, and tests ML model.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def get_data(filename="wine.csv"):
    return pd.read_csv(filename)

def prepare_data(df):
    X = df.drop('Class', axis=1)
    y = df['Class']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def test_model(model, X_test):
    return model.predict(X_test)

def main():
    df = get_data("wine.csv")
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    y_pred = test_model(model, X_test)
    print("Predictions:", y_pred)

if __name__ == "__main__":
    main()
