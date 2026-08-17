############################################################################################################################
#
# Program      : Wine Dataset - Step 1,2,3 (Get + Prepare + Train)
# Functions    : get_data(), prepare_data(), train_model(), main()
# Input        : Wine dataset
# Output       : Trains Decision Tree model
# Description  : Loads, prepares, and trains ML model.
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

def main():
    df = get_data("wine.csv")
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    print("Model trained successfully.")

if __name__ == "__main__":
    main()
