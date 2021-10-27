neighbors = neighbors.NearestNeighbors(n_neighbors=3)
nb_neighbors = neighbors.fit(points)

distances, indices = nb_neighbors.kneighbors()
distances = np.sort(distances, axis=0)
distances = distances[:,1]
eps = np.median(distances) / 2