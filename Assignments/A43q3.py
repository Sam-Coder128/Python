############################################################################################################################
#
# Program      : Play Predictor ML Application - Q3 (Step 1,2,3: Get + Prepare + Train)
# Functions    : get_data(), prepare_data(), train_model(), main()
# Input        : MarvellousInfosystems_PlayPredictor.csv
# Output       : Trains KNN model
# Description  : Loads, prepares, and trains KNN model with K=3.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

def get_data(filename="MarvellousInfosystems_PlayPredictor.csv"):
    return pd.read_csv(filename)

def prepare_data(df):
    le = LabelEncoder()
    df['Weather'] = le.fit_transform(df['Weather'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])
    return df

def train_model(df):
    X = df[['Weather','Temperature']]
    y = df['Play']
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,y)
    print("Model trained successfully.")
    return model

def main():
    df = get_data()
    df = prepare_data(df)
    train_model(df)

if __name__ == "__main__":
    main()
