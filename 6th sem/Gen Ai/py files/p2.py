import matplotlib.pyplot as plt, seaborn as sns, spacy, numpy as np
from sklearn.decomposition import PCA

'''!python -m spacy download en_core_web_md'''

nlp = spacy.load("en_core_web_md")
words = ["computer","internet","software","hardware","network","AI","cloud","cybersecurity","database","robotics"]

vecs = np.array([nlp(w).vector for w in words])
p = PCA(n_components=2).fit_transform(vecs)

plt.figure(figsize=(10,6))
sns.scatterplot(x=p[:,0], y=p[:,1], s=100)

for i,w in enumerate(words):
    plt.annotate(w,(p[i,0],p[i,1]),xytext=(5,5),textcoords="offset points",
                 bbox=dict(fc="white",alpha=.7))

plt.title("PCA Visualization of Word Embeddings")
plt.xlabel("PC1"); plt.ylabel("PC2")
plt.grid(ls="--",alpha=.5)
plt.show()