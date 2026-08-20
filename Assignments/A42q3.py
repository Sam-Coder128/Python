############################################################################################################################
#
# Program      : KNN Classification for Student Performance
# Functions    : euclidean_distance(), knn_predict(), main()
# Input        : Study Hours, Attendance percentage
# Output       : Predicted Result (Pass/Fail)
# Description  : Implements KNN manually using Euclidean distance and majority voting.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import math

# Dataset: (StudyHours, Attendance, Result)
dataset = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

def euclidean_distance(p1, p2):
    return round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2), 2)

def knn_predict(new_point, k=3):
    distances = []
    for (study, attend, label) in dataset:
        dist = euclidean_distance((study, attend), new_point)
        distances.append(((study, attend, label), dist))
    # Sort by distance
    distances.sort(key=lambda x: x[1])
    print("Nearest Neighbors:")
    for i in range(k):
        record, dist = distances[i]
        print(f"Study Hours: {record[0]}, Attendance: {record[1]}, Result: {record[2]}, Distance: {dist}")
    # Majority voting
    labels = [distances[i][0][2] for i in range(k)]
    prediction = max(set(labels), key=labels.count)
    return prediction

def main():
    study = int(input("Enter Study Hours: "))
    attend = int(input("Enter Attendance: "))
    result = knn_predict((study, attend), k=3)
    print("Predicted Result:", result)

if __name__ == "__main__":
    main()
