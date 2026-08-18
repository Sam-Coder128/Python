#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Program      : Wine Quality Classifier
#Functions    : get_data(), prepare_data(), train_model(), test_model(), calculate_accuracy(), main()
#Input        : Wine dataset (CSV file with 13 features + Class)
#Output       : Training and Testing accuracy, Confusion Matrix
#Description  : Complete ML pipeline for wine classification with Decision Tree.
#Author       : Samruddh Shivkumar Birajdar
#----------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : get_data
#Input        : filename (CSV file path)
#Output       : Pandas DataFrame
#Description  : Loads wine dataset from CSV file.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def get_data(filename="wine.csv"):
    df = pd.read_csv(filename)
    print("Dataset loaded. Shape:", df.shape)
    return df

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : prepare_data
#Input        : DataFrame
#Output       : X_train, X_test, y_train, y_test
#Description  : Splits dataset into training and testing sets.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def prepare_data(df):
    X = df.drop('Class', axis=1)
    y = df['Class']
    return train_test_split(X, y, test_size=0.2, random_state=42)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : train_model
#Input        : Training features and labels
#Output       : Trained DecisionTreeClassifier model
#Description  : Trains the decision tree model on training data.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def train_model(X_train, y_train):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : test_model
#Input        : Trained model, Testing features
#Output       : Predictions for test set
#Description  : Uses trained model to predict test data.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def test_model(model, X_test):
    return model.predict(X_test)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Function     : calculate_accuracy
#Input        : True labels, Predicted labels
#Output       : Accuracy score, Confusion Matrix plot
#Description  : Calculates accuracy and displays confusion matrix.
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def calculate_accuracy(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred) * 100
    print("Model Accuracy:", acc, "%")
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[1,2,3])
    disp.plot(cmap="Blues")
    plt.title("Wine Classification Confusion Matrix")
    plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Entry Point Function : main
#Description          : Executes full ML pipeline (Step 1 to 5).
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    df = get_data("wine.csv")
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    y_pred = test_model(model, X_test)
    calculate_accuracy(y_test, y_pred)

if __name__ == "__main__":
    main()
