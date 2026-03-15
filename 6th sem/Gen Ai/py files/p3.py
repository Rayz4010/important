import nltk, numpy as np, matplotlib.pyplot as plt, seaborn as sns
from nltk.corpus import reuters
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

nltk.download("punkt"); nltk.download("reuters"); nltk.download("punkt_tab")

sents = [[w.lower() for w in s if w.isalpha()] for s in reuters.sents()[:5000]]
model = Word2Vec(sents, vector_size=100, window=5, min_count=2, workers=4)

term = "disease"
print(model.wv.most_similar(term, topn=5) if term in model.wv else f"{term} not found")

words = ["health","disease","doctor","patient","treatment","medicine","virus","surgery","nurse","hospital"]
vecs = np.array([model.wv[w] for w in words if w in model.wv])

p = TSNE(n_components=2, random_state=42, perplexity=3).fit_transform(vecs)

plt.figure(figsize=(10,6))
sns.scatterplot(x=p[:,0], y=p[:,1], s=100)

for i,w in enumerate([w for w in words if w in model.wv]):
    plt.annotate(w,(p[i,0],p[i,1]),bbox=dict(fc="white",alpha=.7))

plt.title("t-SNE Visualization of Medical Word Embeddings")
plt.xlabel("Dim 1"); plt.ylabel("Dim 2")
plt.grid(ls="--",alpha=.5)
plt.show()