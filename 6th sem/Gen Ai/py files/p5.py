import random, gensim.downloader as api

model = api.load("word2vec-google-news-300")

def gen_para(seed):
    try: w=[x for x,_ in model.most_similar(seed,topn=5)]
    except: w=[seed]
    random.shuffle(w)
    p=f"Once upon a time a {seed} dreamed of adventure. "
    for i in w: p+=f"It found a {i}, starting a strange journey. "
    return p+"It changed everything."

print(gen_para(input("Seed word: ")))