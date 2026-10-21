import pandas as pd

# Set USE_CSV = True to load your own CSV.
USE_CSV = False
CSV_PATH = "weather.csv"

def get_data():
    if USE_CSV:
        df = pd.read_csv(CSV_PATH)
    else:
        # Inbuilt categorical dataset: last column is the class label.
        df = pd.DataFrame([
            ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
            ["Sunny", "Warm", "High",   "Strong", "Warm", "Same", "Yes"],
            ["Rainy", "Cold", "High",   "Strong", "Warm", "Change", "No"],
            ["Sunny", "Warm", "High",   "Strong", "Cool", "Change", "Yes"],
            ["Rainy", "Warm", "Normal", "Weak",   "Cool", "Same", "No"],
        ], columns=["Sky", "AirTemp", "Humidity", "Wind", "Water", "Forecast", "EnjoySport"])
    return df

def find_s(X, y):
    positive = [row for row, label in zip(X, y) if str(label).lower() in ("yes", "1", "true")]
    if not positive:
        return ["Ø"] * X.shape[1]
    hypothesis = list(positive[0])
    for row in positive[1:]:
        for j, value in enumerate(row):
            if hypothesis[j] != value:
                hypothesis[j] = "?"
    return hypothesis

def candidate_elimination(X, y):
    n = X.shape[1]
    S = ["Ø"] * n
    G = [["?"] * n]

    def covers(h, x):
        return all(a == "?" or a == b for a, b in zip(h, x))

    for row, label in zip(X, y):
        positive = str(label).lower() in ("yes", "1", "true")
        row = list(row)

        if positive:
            G = [g for g in G if covers(g, row)]
            if S == ["Ø"] * n:
                S = row.copy()
            else:
                for j in range(n):
                    if S[j] != row[j]:
                        S[j] = "?"
            G = [g for g in G if covers(g, row)]
        else:
            new_G = []
            for g in G:
                if not covers(g, row):
                    new_G.append(g)
                    continue
                for j in range(n):
                    if S[j] == "?":
                        continue
                    if S[j] != "Ø" and S[j] != row[j]:
                        candidate = g.copy()
                        candidate[j] = S[j]
                        if covers(candidate, row) is False:
                            new_G.append(candidate)
            # Remove duplicates and hypotheses that are more specific than another G.
            unique = []
            for h in new_G:
                if h not in unique:
                    unique.append(h)
            G = unique

    return S, G

if __name__ == "__main__":
    df = get_data()
    X = df.iloc[:, :-1].astype(str).to_numpy()
    y = df.iloc[:, -1].astype(str).to_numpy()

    print("Dataset:\n", df.to_string(index=False))
    print("\nFind-S final hypothesis:", find_s(X, y))
    S, G = candidate_elimination(X, y)
    print("Candidate Elimination:")
    print("S (specific boundary):", S)
    print("G (general boundary):")
    for h in G:
        print(" ", h)
