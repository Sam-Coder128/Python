############################################################################################################################
#
# Program      : Confusion Matrix
# Functions    : confusion_matrix_demo(), main()
# Input        : student_performance_ml.csv
# Output       : Displays confusion matrix
# Description  : Generates confusion matrix and explains TP, TN, FP, FN.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def confusion_matrix_demo(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    print("Confusion Matrix:\n", cm)
    print("TP: Correctly predicted Pass")
    print("TN: Correctly predicted Fail")
    print("FP: Predicted Pass but actually Fail")
    print("FN: Predicted Fail but actually Pass")

def main():
    confusion_matrix_demo("student_performance_ml.csv")

if __name__ == "__main__":
    main()
