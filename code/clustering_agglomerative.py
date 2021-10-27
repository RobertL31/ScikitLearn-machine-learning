# -*- coding: utf-8 -*-
"""
Authors : Julien Rouzot, Loïc Robert
"""

from scipy.io import arff
from matplotlib import pyplot as plt    
from sklearn import cluster, metrics
import time
import math


# the filenames to load, k-means should be efficient on these 3 files
filenames = [
  "artificial/2d-3c-no123.arff",
  "artificial/R15.arff",
  "artificial/spiral.arff",
  "artificial/pathbased.arff",
]

# load the data with arff

filename = filenames[2]

data = arff.loadarff(open(filename, 'r'))[0]
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
"""  


max_silhouette_score = -1
max_davies_bouldin_score = math.inf
max_calvinski_harabasz_score = 0
best_nb_clusters = -1
    
# Compute time to find the best nb of clusters
start_time = time.time()

for i in range(2, 50):
    n_clusters = i 
    
    agglo = cluster.AgglomerativeClustering(n_clusters).fit(points)
    
    current_silhouette_score = metrics.silhouette_score(points, agglo.labels_)
    if current_silhouette_score >= max_silhouette_score:
        max_silhouette_score = current_silhouette_score
        best_nb_clusters = i
      


print("filename : %s" % filename.split("/")[1])
print("time : %s" % (time.time() - start_time))

# Apply k-means with the target nb_clusters
agglo = cluster.AgglomerativeClustering(n_clusters=best_nb_clusters, linkage='ward').fit(points)  
print("nb_clusters : " + str(agglo.labels_.max() + 1))

if len(points[0]) == 2:
  # plot 2D
  fig = plt.scatter(*zip(*points), c=agglo.labels_)
elif len(points[0]) == 3:
  # plot 3D
  ax = plt.axes(projection='3d')
  ax.scatter3D(*zip(*points), c=agglo.labels_)
else:
  print("Can't plot more than 3 dimensions")




