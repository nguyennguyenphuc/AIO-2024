import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# Load Iris dataset
iris_dataset = load_iris()
data = iris_dataset.data[:, :2]  # Use only the first two features

# Plot the initial dataset
plt.scatter(data[:, 0], data[:, 1], c='gray')
plt.title("Initial Dataset")
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()

# Build K-Means model and fit data
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)

# Plot clusters and centroids
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_,
            cmap='viridis', marker='o', alpha=0.6)
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    s=300, c='red', marker='x'
)
plt.title("Clusters and Centroids")
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
