############################################################################################################################
#
# Program      : Count Pass and Fail Students
# Functions    : analyze_results(), main()
# Input        : student_performance_ml.csv
# Output       : Total students, Pass count, Fail count
# Description  : Uses pandas to count students based on FinalResult.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def analyze_results(filename):
    df = pd.read_csv(filename)
    total = len(df)
    passed = (df['FinalResult'] == 1).sum()
    failed = (df['FinalResult'] == 0).sum()
    print("Total students:", total)
    print("Passed:", passed)
    print("Failed:", failed)

def main():
    analyze_results("student_performance_ml.csv")

if __name__ == "__main__":
    main()
