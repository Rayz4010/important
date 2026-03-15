import openai
openai.api_key = "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"

r = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"honesty is the best"}],
    n=3, temperature=1
)

for i,c in enumerate(r.choices,1):
    print(f"--- Response {i} ---\n{c.message.content}\n")