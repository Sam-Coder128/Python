############################################################################################################################
#
# Program      : Play Predictor ML Application - Q2 (Step 1 & 2: Get + Prepare Data)
# Functions    : get_data(), prepare_data(), main()
# Input        : MarvellousInfosystems_PlayPredictor.csv
# Output       : Encoded dataset
# Description  : Loads dataset and encodes categorical features using LabelEncoder.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def get_data(filename="MarvellousInfosystems_PlayPredictor.csv"):
    return pd.read_csv(filename)

def prepare_data(df):
    le = LabelEncoder()
    df['Weather'] = le.fit_transform(df['Weather'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])
    print("Encoded Data:\n", df.head())
    return df

def main():
    df = get_data()
    df = prepare_data(df)

if __name__ == "__main__":
    main()
