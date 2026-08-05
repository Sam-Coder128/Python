############################################################################################################################
#
# Program      : Analyze FinalResult Distribution
# Functions    : analyze_distribution(), main()
# Input        : student_performance_ml.csv
# Output       : Value counts, Percentages, Balance check
# Description  : Uses value_counts() to analyze distribution of FinalResult.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def analyze_distribution(filename):
    df = pd.read_csv(filename)
    counts = df['FinalResult'].value_counts()
    percentages = df['FinalResult'].value_counts(normalize=True) * 100
    print("Distribution:\n", counts)
    print("\nPercentages:\n", percentages)
    if abs(percentages[0] - percentages[1]) < 10:
        print("\nDataset is fairly balanced.")
    else:
        print("\nDataset is imbalanced.")

def main():
    analyze_distribution("student_performance_ml.csv")

if __name__ == "__main__":
    main()
