############################################################################################################################
#
# Program      : Decision Tree Visualization
# Functions    : visualize_tree(), main()
# Input        : student_performance_ml.csv
# Output       : Plots decision tree
# Description  : Uses sklearn plot_tree to visualize trained decision tree.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

def visualize_tree(filename):
    df = pd.read_csv(filename)
    X = df.drop('FinalResult', axis=1)
    y = df['FinalResult']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    plt.figure(figsize=(12,8))
    plot_tree(model, feature_names=X.columns, class_names=['Fail','Pass'], filled=True)
    plt.show()
    print("Root node feature likely chosen based on highest information gain.")

def main():
    visualize_tree("student_performance_ml.csv")

if __name__ == "__main__":
    main()
