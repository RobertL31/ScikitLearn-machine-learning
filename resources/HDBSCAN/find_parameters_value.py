max_silhouette_score = -1
best_eps = -1
best_min_samples = -1

# Compute time to find the best eps and min_samples params
start_time = time.time()

# let's loop to find best eps and nb_samples
for i in range(1, 20):
  
  min_samples = 1
  
  for i in range(1, 10):
    
    clusterer = hdbscan.HDBSCAN(cluster_selection_epsilon=float(eps), min_samples=min_samples).fit(points)
    
    # Number of clusters
    n_clusters_ = clusterer.labels_.max() + 1

    if n_clusters_ <= 1:
      break
    
    current_silhouette_score = metrics.silhouette_score(points, clusterer.labels_)
    if current_silhouette_score >= max_silhouette_score:
        max_silhouette_score = current_silhouette_score
        best_eps = eps
        best_min_samples = min_samples
      
    min_samples += 1
    
  eps += np.median(distances)
  

print("filename : %s" % filename.split("/")[1])
print("time : %s" % (time.time() - start_time))

clusterer = hdbscan.HDBSCAN(cluster_selection_epsilon=float(best_eps), min_samples=best_min_samples).fit(points)
print("nb_clusters : " + str(clusterer.labels_.max() + 1))