############################################################################################################################
#
# Program      : Play Predictor ML Application
# Functions    : get_data(), main()
# Input        : MarvellousInfosystems_PlayPredictor.csv
# Output       : Displays dataset shape and first few records
# Description  : Loads dataset into Python application.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def get_data(filename="MarvellousInfosystems_PlayPredictor.csv"):
    df = pd.read_csv(filename)
    print("Dataset Shape:", df.shape)
    print("First 5 records:\n", df.head())
    return df

def main():
    df = get_data()

if __name__ == "__main__":
    main()
