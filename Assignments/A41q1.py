############################################################################################################################
#
# Program      : Wine Dataset - Step 1 (Get Data)
# Functions    : get_data(), main()
# Input        : Wine dataset (CSV or sklearn)
# Output       : Displays first few records and shape
# Description  : Loads wine dataset for classification.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def get_data(filename="wine.csv"):
    df = pd.read_csv(filename)
    print("Dataset Shape:", df.shape)
    print("First 5 records:\n", df.head())
    return df

def main():
    df = get_data("wine.csv")

if __name__ == "__main__":
    main()
