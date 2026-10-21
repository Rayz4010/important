import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Inbuilt Iris dataset. No CSV download required.
iris = load_iris(as_frame=True)
X = iris.data

# Scale numeric features before clustering.
X_scaled = StandardScaler().fit_transform(X)

# Elbow method: compare inertia for k = 1..10.
inertias = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    inertias.append(model.inertia_)

plt.plot(range(1, 11), inertias, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

# Run final clustering. Change n_clusters to experiment.
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

result = X.copy()
result["Cluster"] = clusters
print(result.head(10).to_string(index=False))

# PCA reduces four features to two dimensions for plotting.
points_2d = PCA(n_components=2).fit_transform(X_scaled)
plt.scatter(points_2d[:, 0], points_2d[:, 1], c=clusters)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering on Iris")
plt.show()
