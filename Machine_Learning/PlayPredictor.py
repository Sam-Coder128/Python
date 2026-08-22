#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Program      : Play Predictor ML Application
#Functions    : get_data(), prepare_data(), train_model(), test_model(), check_accuracy(), main()
#Input        : PlayPredictor.csv
#Output       : Prediction + Accuracy
#Description  : Complete ML pipeline with accuracy calculation using KNN.
#Author       : Samruddh Shivkumar Birajdar
#----------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : get_data
#Input        : filename (CSV file path)
#Output       : Pandas DataFrame
#Description  : Loads Play Predictor dataset from CSV file.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def get_data(filename="PlayPredictor.csv"):
    return pd.read_csv(filename)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : prepare_data
#Input        : DataFrame
#Output       : Prepared Pandas DataFrame
#Description  : Converts categorical data into numerical values using LabelEncoder.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def prepare_data(df):
    le = LabelEncoder()

    df['Weather'] = le.fit_transform(df['Weather'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])

    return df

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : train_model
#Input        : Training features, Training labels, K value
#Output       : Trained KNeighborsClassifier model
#Description  : Creates and trains the KNN classification model.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def train_model(X_train, y_train, k=3):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return model

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : test_model
#Input        : Trained model, Testing features
#Output       : Predictions for test set
#Description  : Uses the trained KNN model to predict test data.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def test_model(model, X_test):
    return model.predict(X_test)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : check_accuracy
#Input        : Prepared DataFrame, K value
#Output       : Accuracy score
#Description  : Splits the dataset, trains the model, predicts test data
#               and calculates the model accuracy.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def check_accuracy(df, k=3):

    X = df[['Weather', 'Temperature']]
    y = df['Play']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.5,
        random_state=42
    )

    model = train_model(X_train, y_train, k)

    y_pred = test_model(model, X_test)

    acc = accuracy_score(y_test, y_pred) * 100

    print("Accuracy with K =", k, ":", acc, "%")

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Entry Point Function : main
#Description          : Executes full ML pipeline for different K values.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    df = get_data("PlayPredictor.csv")

    df = prepare_data(df)

    check_accuracy(df, k=1)
    check_accuracy(df, k=3)
    check_accuracy(df, k=5)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
