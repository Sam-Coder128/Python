############################################################################################################################
#
# Program      : KNN Prediction with Different K
# Functions    : euclidean_distance(), knn_predict(), main()
# Input        : Dataset points (X,Y,Label), new point coordinates
# Output       : Predictions for K=1, K=3, K=5
# Description  : Demonstrates how prediction changes with different K values.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import math

# Dataset
dataset = {
    "A": (1, 2, "Red"),
    "B": (2, 3, "Red"),
    "C": (3, 1, "Blue"),
    "D": (6, 5, "Blue")
}

def euclidean_distance(p1, p2):
    return round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2), 2)

def knn_predict(new_point, k):
    distances = []
    for key, (x,y,label) in dataset.items():
        dist = euclidean_distance((x,y), new_point)
        distances.append((key, dist, label))
    distances.sort(key=lambda x: x[1])
    labels = [distances[i][2] for i in range(min(k,len(distances)))]
    prediction = max(set(labels), key=labels.count)
    return prediction

def main():
    new_point = (2,2)
    print("Prediction Results")
    print("K = 1 →", knn_predict(new_point, 1))
    print("K = 3 →", knn_predict(new_point, 3))
    print("K = 5 →", knn_predict(new_point, 5))
    print("\nExplanation:")
    print("With small K (1 or 3), nearby Red points dominate → prediction is Red.")
    print("With larger K (5), Blue points are included more → prediction shifts to Blue.")

if __name__ == "__main__":
    main()
