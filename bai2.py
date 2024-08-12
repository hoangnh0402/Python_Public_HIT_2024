import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

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

# Hàm phân cấp để gom cụm
def hierarchical_clustering(points, method='single'):
    linked = linkage(points, method=method)
    dendrogram(linked,
               orientation='top',
               distance_sort='descending',
               show_leaf_counts=True)
    plt.title(f'Hierarchical Clustering Dendrogram ({method} linkage)')
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    plt.show()

# Phân cụm với liên kết đơn
hierarchical_clustering(points, method='single')

# Phân cụm với liên kết đầy đủ
hierarchical_clustering(points, method='complete')
