"""
!pip install gensim
"""

import gensim.downloader as api

model = api.load("word2vec-google-news-300")

print("Similarity:", model.similarity("king", "queen"))

print("King - Man + Woman:",
      model.most_similar(positive=["king","woman"], negative=["man"], topn=1)[0])

print("Similar to Paris:")
for w,s in model.most_similar("Paris", topn=5):
    print(w, s)

print("Odd one out:",
      model.doesnt_match(["breakfast","lunch","dinner","banana"]))