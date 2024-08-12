import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dữ liệu điểm
points = np.array([
    [1, 1],
    [1, 3],
    [2, 2],
    [4, 4],
    [4, 5],
    [5, 4],
    [5, 5]
])

# Hàm K-means clustering
def kmeans_clustering(points, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(points)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Vẽ đồ thị kết quả
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red')
    plt.title(f'K-means clustering with K={k}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# Nhập số cụm K từ bàn phím
k = int(input("Nhập số cụm K: "))
kmeans_clustering(points, k)
