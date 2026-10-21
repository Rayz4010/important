# Install first: pip install minisom scikit-learn matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

iris = load_iris()
X = iris.data
X_scaled = MinMaxScaler().fit_transform(X)

# Change grid dimensions, sigma, learning_rate, and iterations to experiment.
som = MiniSom(x=10, y=10, input_len=X_scaled.shape[1],
              sigma=1.0, learning_rate=0.5, random_seed=42)
som.random_weights_init(X_scaled)
som.train_random(X_scaled, num_iteration=1000)

# U-Matrix shows distances between neighboring SOM neurons.
plt.figure(figsize=(8, 7))
plt.pcolor(som.distance_map().T, cmap="coolwarm")
plt.colorbar(label="Neighbor distance")
plt.title("SOM U-Matrix")
plt.show()

# Plot each data point at its winning neuron; colors indicate Iris class.
plt.figure(figsize=(8, 7))
plt.pcolor(som.distance_map().T, cmap="coolwarm", alpha=0.5)
markers = ["o", "s", "D"]
colors = ["red", "green", "blue"]
for row, label in zip(X_scaled, iris.target):
    winner_x, winner_y = som.winner(row)
    plt.plot(winner_x + 0.5, winner_y + 0.5,
             markers[label], markerfacecolor="None",
             markeredgecolor=colors[label], markersize=8)
plt.title("SOM Winning Neurons (color = Iris class)")
plt.show()

# Print winning neuron for each sample.
for i, row in enumerate(X_scaled[:10]):
    print(f"Sample {i + 1}: winning neuron = {som.winner(row)}")
