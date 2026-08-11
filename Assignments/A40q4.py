############################################################################################################################
#
# Program      : Predict New Students
# Functions    : predict_new(), main()
# Input        : student_performance_ml.csv
# Output       : Predictions for 5 new students
# Description  : Trains model and predicts results for new student DataFrame.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def predict_new(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    new_students = pd.DataFrame({
        'StudyHours':[2,5,1,4,3],
        'Attendance':[80,95,60,85,70],
        'PreviousScore':[50,75,40,65,55],
        'AssignmentsCompleted':[5,10,2,8,6],
        'SleepHours':[7,6,5,8,7]
    })
    preds = model.predict(new_students)
    print("Predictions for new students:", preds)

def main():
    predict_new("student_performance_ml.csv")

if __name__ == "__main__":
    main()
