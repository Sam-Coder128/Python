############################################################################################################################
#
# Program      : Complete ML Pipeline for Student Performance
# Functions    : load_data(), analyze_data(), visualize_data(), split_data(), train_model(), evaluate_model(), main()
# Input        : student_performance_ml.csv
# Output       : Dataset info, plots, train/test split, model training, predictions, accuracy, confusion matrix
# Description  : End-to-end ML workflow with Decision Tree classifier.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def load_data(filename):
    df = pd.read_csv(filename)
    print("Dataset loaded. Shape:", df.shape)
    return df

def analyze_data(df):
    print("First 5 records:\n", df.head())
    print("Column info:\n", df.dtypes)
    print("Pass/Fail distribution:\n", df['FinalResult'].value_counts())

def visualize_data(df):
    df['FinalResult'].value_counts().plot(kind='bar', title="Pass vs Fail")
    plt.show()

def split_data(df):
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_train, X_test, y_train, y_test):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred) * 100
    print("Accuracy:", acc, "%")
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(confusion_matrix=cm).plot()
    plt.show()

def main():
    df = load_data("student_performance_ml.csv")
    analyze_data(df)
    visualize_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
