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