############################################################################################################################
#
# Program      : Play Predictor ML Application - Q4 (Step 1,2,3,4: Get + Prepare + Train + Test)
# Functions    : get_data(), prepare_data(), train_model(), test_model(), main()
# Input        : MarvellousInfosystems_PlayPredictor.csv
# Output       : Prediction for new input
# Description  : Tests trained KNN model with user input.
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
    return df, le

def train_model(df):
    X = df[['Weather','Temperature']]
    y = df['Play']
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,y)
    return model

def test_model(model, le):
    weather = input("Enter Weather (Sunny/Overcast/Rainy): ")
    temp = input("Enter Temperature (Hot/Mild/Cold): ")
    weather_enc = le.fit_transform([weather])[0]
    temp_enc = le.fit_transform([temp])[0]
    prediction = model.predict([[weather_enc,temp_enc]])[0]
    print("Predicted Result:", "Yes" if prediction==1 else "No")

def main():
    df = get_data()
    df, le = prepare_data(df)
    model = train_model(df)
    test_model(model, le)

if __name__ == "__main__":
    main()
