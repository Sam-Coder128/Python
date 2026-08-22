############################################################################################################################
#
# Program      : Play Predictor ML Application - Q5 (Step 1 to 5: Full Pipeline with Accuracy)
# Functions    : get_data(), prepare_data(), train_model(), test_model(), check_accuracy(), main()
# Input        : MarvellousInfosystems_PlayPredictor.csv
# Output       : Prediction + Accuracy
# Description  : Complete ML pipeline with accuracy calculation using KNN.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def get_data(filename="MarvellousInfosystems_PlayPredictor.csv"):
    return pd.read_csv(filename)

def prepare_data(df):
    le = LabelEncoder()
    df['Weather'] = le.fit_transform(df['Weather'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])
    return df

def train_model(X_train, y_train, k=3):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return model

def test_model(model, X_test):
    return model.predict(X_test)

def check_accuracy(df, k=3):
    X = df[['Weather','Temperature']]
    y = df['Play']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5,random_state=42)
    model = train_model(X_train,y_train,k)
    y_pred = test_model(model,X_test)
    acc = accuracy_score(y_test,y_pred)*100
    print(f"Accuracy with K={k}:", acc, "%")

def main():
    df = get_data()
    df = prepare_data(df)
    check_accuracy(df, k=1)
    check_accuracy(df, k=3)
    check_accuracy(df, k=5)

if __name__ == "__main__":
    main()
