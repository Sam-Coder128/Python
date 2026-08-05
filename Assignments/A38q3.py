############################################################################################################################
#
# Program      : Calculate Statistics
# Functions    : calculate_stats(), main()
# Input        : student_performance_ml.csv
# Output       : Average StudyHours, Average Attendance, Max PreviousScore, Min SleepHours
# Description  : Uses pandas functions to calculate statistics on dataset.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def calculate_stats(filename):
    df = pd.read_csv(filename)
    print("Average StudyHours:", df['StudyHours'].mean())
    print("Average Attendance:", df['Attendance'].mean())
    print("Maximum PreviousScore:", df['PreviousScore'].max())
    print("Minimum SleepHours:", df['SleepHours'].min())

def main():
    calculate_stats("student_performance_ml.csv")

if __name__ == "__main__":
    main()
