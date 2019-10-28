import random
import csv
import math
import sys
import numpy as np
from operator import add 
from prettytable import PrettyTable

def find_dist(row,centroid):
    result = 0
    for i in range(len(row)):
        result += math.pow(row[i]-centroid[i],2)
    result = math.sqrt(result)
    return result


def fuzzy_clustering(dataset,n_attr,c,m):
    prev_centroids = [[random.uniform(0,100) for j in range(n_attr)] for i in range(c)]
    next_centroids = list()

    iterations = 0

    while iterations < 50:
        membership_matrix = [[0 for i in range(c)] for j in range(len(dataset))]
        clusters = [[] for i in range(c)]

        # Calculating membership matrix
        for row_index in range(len(dataset)):
            # hardcoding
            x_m_c1 = find_dist(dataset[row_index][:-1],prev_centroids[0])
            x_m_c2 = find_dist(dataset[row_index][:-1],prev_centroids[1]) 

            u_x_c1 = 1/( 1 + math.pow(x_m_c1/x_m_c2,2/(m-1)) )
            u_x_c2 = 1/( 1 + math.pow(x_m_c2/x_m_c1,2/(m-1)) )   

            membership_matrix[row_index][0] = u_x_c1
            membership_matrix[row_index][1] = u_x_c2

            if u_x_c1 > u_x_c2:
                clusters[0].append(row_index)
            else:
                clusters[1].append(row_index)

        for cluster_index in range(len(clusters)):
            numerator = [0 for i in range(n_attr)]
            denominator = 0
            for row_index in clusters[cluster_index]:
                u_i_j_m = math.pow(membership_matrix[row_index][cluster_index],m)
                num_temp = [x*u_i_j_m for x in dataset[row_index][:-1]]
                numerator = list(map(add, numerator, num_temp)) 
                denominator += u_i_j_m
            
            if denominator == 0:
                denominator = 1
            centroid = [math.floor(x/denominator) for x in numerator]
            next_centroids.append(centroid)

        if(prev_centroids == next_centroids):
            break

        prev_centroids = next_centroids[::]
        next_centroids = list()

        iterations += 1
    
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for pred_class in range(len(clusters)):
        for row_index in clusters[pred_class]:
            if pred_class == 0 and dataset[row_index][-1] == 0:
                tn += 1
            if pred_class == 0 and dataset[row_index][-1] == 1:
                fn += 1
            if pred_class == 1 and dataset[row_index][-1] == 0:
                fp += 1
            if pred_class == 1 and dataset[row_index][-1] == 1:
                tp += 1

    t = PrettyTable([' ', 'Predicted Yes', 'Predicted No'])
    t.add_row(['Actual Yes', tp, fn])
    t.add_row(['Actual No', fp, tn])
    print(t)

    print("Precision: " + str(float((tp/(tp+fp))*100)) + "%")
    print("Recall: " + str(float((tp/(tp+fn))*100)) + '%')

    return ((tp+tn)/(tp+fp+tn+fn))


def main():
    filename = 'SPECTF.csv'
    dataset = []
    n_attr = 0

    with open(filename,'r') as file:
        len_attributes = 0
        i = 0
        for line in file:
            if (i==0):
                i = 1
                continue
            row_ = line.split(',')

            if(n_attr==0):
                n_attr = len(row_) - 1

            if(len_attributes==0):
                len_attributes = len(row_) - 1
            
            if row_[0] == 'No':
                row_[0] = '0.0'
            else:
                row_[0] = '1.0'
            

            # Use if class at start
            row_ = row_[1:] + [row_[0]]
            
            row = [float(x) for x in row_]
            dataset.append(row)

    c = 2
    m = 2

    accuracy = fuzzy_clustering(dataset,n_attr,c,m)
    # if (accuracy<0.5):
        # accuracy = 1 - accuracy
    print('Accuracy is ' + str(accuracy*100) + '%')
    
if __name__ == '__main__':
    main()
