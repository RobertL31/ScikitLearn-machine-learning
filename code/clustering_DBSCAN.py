#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:01:25 2021

@author: julien
"""

from scipy.io import arff
from matplotlib import pyplot as plt 
from sklearn import cluster, metrics, neighbors  

import numpy as np
import time
import math

"""
# the filenames to load, k-means should be efficient on these 3 files
filenames = [
  "artificial/spiral.arff",
  "artificial/banana.arff",
  "artificial/smile1.arff" 
]

# load the data with arff
data = arff.loadarff(open(filenames[1], 'r'))[0]
points = []

# Extract data from arff file
for x, y, z in data:
    points.append([x, y])
"""

synthese_filenames = [
  "dataset/a.data",
  "dataset/h.data",
  "dataset/t.data",
  "dataset/tr.data",
  "dataset/zgn.data",
  "dataset/zgo.data"
]

# parse the txt file to extract points
def parse_txt(filename):
  data = []
  with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
      raw_data = line.split()
      clean_data = []    
      for el in raw_data:
        clean_data.append(float(el))
      data.append(clean_data)
  return data
           

# load the txt data
filename = synthese_filenames[5]
points = parse_txt(filename)
    
neighbors = neighbors.NearestNeighbors(n_neighbors=3)
nb_neighbors = neighbors.fit(points)

distances, indices = nb_neighbors.kneighbors()
distances = np.sort(distances, axis=0)
distances = distances[:,1]
eps = np.median(distances) / 2

max_silhouette_score = -1
max_davies_bouldin_score = math.inf
max_calvinski_harabasz_score = 0
best_eps = eps
best_min_samples = 2


# Compute time to find the best eps and min_samples params
start_time = time.time()

# let's loop to find best eps and nb_samples
for i in range(1, 20):
  
  min_samples = 2
  
  for i in range(1, 10):
    
    dbscan = cluster.DBSCAN(eps=eps, min_samples=min_samples).fit(points)
    
    # Number of clusters
    n_clusters_ = dbscan.labels_.max() + 1

    if n_clusters_ <= 1:
      break
    
    current_silhouette_score = metrics.silhouette_score(points, dbscan.labels_)
    if current_silhouette_score >= max_silhouette_score:
        max_silhouette_score = current_silhouette_score
        best_eps = eps
        best_min_samples = min_samples
      
    min_samples += math.ceil((len(points) / 2000))
    
  eps += np.median(distances) / 2
  
print("filename : %s" % filename.split("/")[1])
print("time : %s" % (time.time() - start_time))

dbscan = cluster.DBSCAN(eps=best_eps, min_samples=best_min_samples).fit(points)
print("nb_clusters : " + str(dbscan.labels_.max() + 1))


if len(points[0]) == 2:
  # plot 2D
  fig = plt.scatter(*zip(*points), c=dbscan.labels_)
elif len(points[0]) == 3:
  # plot 3D
  ax = plt.axes(projection='3d')
  ax.scatter3D(*zip(*points), c=dbscan.labels_)
else:
  print("Can't plot more than 3 dimensions")
