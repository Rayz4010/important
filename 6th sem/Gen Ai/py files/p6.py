from transformers import pipeline

sent = pipeline("sentiment-analysis")

while True:
    t = input("Enter sentence (exit to quit): ")
    if t.lower() == "exit": break
    r = sent(t)[0]
    print(f"Sentiment: {r['label']} (Confidence: {r['score']:.2f})\n")