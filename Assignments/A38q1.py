############################################################################################################################
#
# Program      : Load Student Performance Dataset
# Functions    : load_data(), main()
# Input        : student_performance_ml.csv
# Output       : First 5 records, Last 5 records, Shape, Column names, Data types
# Description  : Loads dataset using pandas and displays basic information.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def load_data(filename):
    df = pd.read_csv(filename)
    print("First 5 records:\n", df.head())
    print("\nLast 5 records:\n", df.tail())
    print("\nTotal rows and columns:", df.shape)
    print("\nColumn names:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)

def main():
    load_data("student_performance_ml.csv")

if __name__ == "__main__":
    main()
