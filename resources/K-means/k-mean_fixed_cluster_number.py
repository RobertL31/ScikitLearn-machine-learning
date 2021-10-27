# load the txt data
filename = filenames[1]

# load the data with arff
data = arff.loadarff(open(filename, 'r'))[0]
points = []

# Extract data from arff file
for x, y, z in data:
    points.append([x, y])

# apply k means
k_means = cluster.KMeans(31).fit(points)


if len(points[0]) == 2:
  # plot 2D
  fig = plt.scatter(*zip(*points), c=k_means.labels_)
elif len(points[0]) == 3:
  # plot 3D
  ax = plt.axes(projection='3d')
  ax.scatter3D(*zip(*points), c=k_means.labels_)
else:
  print("Can't plot more than 3 dimensions")