#importing libraries
import pandas as pd
import numpy as np
import statistics as st
import math
import matplotlib.pyplot as plt

#importing dataset
data = pd.read_csv("kmeans_test.csv")

#converting columns to list
x = list(data['x'].values)
y = list(data['y'].values)

#initializing clusters
cluster1_x, cluster1_y, cluster2_x, cluster2_y = [], [], [], []

#initially taking centroids as 1st 2 records
N_centroids = 2
centroids = []
for i in range(N_centroids):
	centroids.append([x[i], y[i]])

print("\nIteration 1")
print("The Centroids Are: {} & {}\n".format(centroids[0], centroids[1]))

#calculating distance
def distance(X, Y, Xc, Yc):
	x_square = (X - Xc) ** 2
	y_square = (Y - Yc) ** 2
	return math.sqrt(x_square + y_square)

#calculating cluster distance for each point
def centroidFunction():
	#each index in C is a list of all distances from centroids
	C = []		
	minimum = 1000000
	C_assign = []
	cluster1 = []
	cluster2 = []

	for i in range(len(x)):
		cluster = []
		for j in range(N_centroids):
			temp = distance(x[i], y[i], centroids[j][0], centroids[j][1])
			cluster.append(round(temp,2))
			if temp < minimum:
				min_index = j
				minimum = temp
		C_assign.append(min_index)
		if min_index == 0:
			cluster1.append([x[i], y[i]])
		else:
			cluster2.append([x[i], y[i]])
		C.append(cluster)
		minimum = 1000000
	
	#printing data
	print("\tx\t\t y\t\tC1{}\tC2{}\tCluster Assigned".format(centroids[0],centroids[1]))
	print("___________"*10)
	for i in range(len(x)):
		print("\t{}\t\t {}\t\t{}\t\t{} \t\t\t{}".format(x[i], y[i], C[i][0], C[i][1], C_assign[i] + 1))
	
	#calculating centroids for next iteration
	centroids.clear()

	#calculating centroid 1
	centroid1_x = 0.0
	centroid1_y = 0.0
	for i in range(len(cluster1)):
		centroid1_x = centroid1_x + cluster1[i][0]
		centroid1_y = centroid1_y + cluster1[i][1]
	centroid1_x = centroid1_x / len(cluster1)
	centroid1_y = centroid1_y / len(cluster1)

	centroids.append([round(centroid1_x,2), round(centroid1_y,2)])

	#calculating centroid 2
	centroid2_x = 0.0
	centroid2_y = 0.0
	for i in range(len(cluster2)):
		centroid2_x = centroid2_x + cluster2[i][0]
		centroid2_y = centroid2_y + cluster2[i][1]
	centroid2_x = centroid2_x / len(cluster2)
	centroid2_y = centroid2_y / len(cluster2)

	centroids.append([round(centroid2_x,2), round(centroid2_y,2)])


	#Visualizing the Results
	cluster1_x.clear() 
	cluster1_y.clear() 
	cluster2_x.clear()
	cluster2_y.clear()
	for i in range(len(cluster1)):
		cluster1_x.append(cluster1[i][0])
		cluster1_y.append(cluster1[i][1])

	for i in range(len(cluster2)):
		cluster2_x.append(cluster2[i][0])
		cluster2_y.append(cluster2[i][1])
	
	
	return C_assign

#iteration 1 assigned clusters
C_assign1 = []
C_assign1 = centroidFunction()

#checking if clusters are same
def checkCluster(clust1, clust2):
	check = 0
	for i in range(len(clust1)):
		if clust1[i] == clust2[i]:
			pass
		else:
			check = check + 1
	return check

print("\nIteration 2")
print("The Centroids Are: {} & {}\n".format(centroids[0], centroids[1]))
#iteration 2 assigned clusters

C_assign2 = []
C_assign2 = centroidFunction()

check = checkCluster(C_assign1, C_assign2)
iteration = 2

while check != 0 or iteration < 10:
	iteration = iteration + 1
	print("\nIteration {}".format(iteration))
	print("The Centroids Are: {} & {}\n".format(centroids[0], centroids[1]))
	C_assign_N = []
	C_assign_N = centroidFunction()
	check = checkCluster(C_assign2, C_assign_N)
	C_assign2.clear()
	C_assign2 = C_assign_N
	if check == 0:
		break

if check == 0:
	print("\nThere is No Change is Cluster Assignment! And Therefore Converge")
else:
	print("Ran Out of Iterations")

#Visualizing the Results
plt.scatter(cluster1_x, cluster1_y, color = 'red')
plt.scatter(cluster2_x, cluster2_y, color = 'blue')
plt.title('K-MEANS')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
