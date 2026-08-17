############################################################################################################################
#
# Program      : Wine Dataset - Step 1 & 2 (Get + Prepare Data)
# Functions    : get_data(), prepare_data(), main()
# Input        : Wine dataset
# Output       : Splits into features and target
# Description  : Loads and prepares dataset for ML.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split

def get_data(filename="wine.csv"):
    df = pd.read_csv(filename)
    return df

def prepare_data(df):
    X = df.drop('Class', axis=1)
    y = df['Class']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def main():
    df = get_data("wine.csv")
    X_train, X_test, y_train, y_test = prepare_data(df)
    print("Training samples:", X_train.shape[0])
    print("Testing samples:", X_test.shape[0])

if __name__ == "__main__":
    main()
