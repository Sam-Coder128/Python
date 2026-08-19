############################################################################################################################
#
# Program      : Manual KNN Classification (K=3)
# Functions    : euclidean_distance(), knn_predict(), main()
# Input        : Dataset points (X,Y,Label), new point coordinates
# Output       : Distances, nearest neighbors, predicted class
# Description  : Implements KNN manually without ML libraries.
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

def knn_predict(new_point, k=3):
    distances = []
    for key, (x,y,label) in dataset.items():
        dist = euclidean_distance((x,y), new_point)
        distances.append((key, dist, label))
    # Sort by distance
    distances.sort(key=lambda x: x[1])
    print("Nearest Neighbors:")
    for i in range(k):
        print(f"{distances[i][0]} - Distance: {distances[i][1]} - Label: {distances[i][2]}")
    # Majority voting
    labels = [distances[i][2] for i in range(k)]
    prediction = max(set(labels), key=labels.count)
    print("Predicted Class:", prediction)

def main():
    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))
    knn_predict((x,y), k=3)

if __name__ == "__main__":
    main()
