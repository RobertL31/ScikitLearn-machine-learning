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