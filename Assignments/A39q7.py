############################################################################################################################
#
# Program      : Predict Single Student Result
# Functions    : predict_student(), main()
# Input        : Student details
# Output       : Pass or Fail prediction
# Description  : Uses trained model to predict result for given student.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def predict_student(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    student = pd.DataFrame({
        'StudyHours':[6],
        'Attendance':[85],
        'PreviousScore':[66],
        'AssignmentsCompleted':[7],
        'SleepHours':[7]
    })
    result = model.predict(student)[0]
    print("Prediction: Pass" if result==1 else "Prediction: Fail")

def main():
    predict_student("student_performance_ml.csv")

if __name__ == "__main__":
    main()
