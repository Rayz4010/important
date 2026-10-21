import pandas as pd
from itertools import combinations

USE_CSV = False
CSV_PATH = "weather.csv"

def get_data():
    if USE_CSV:
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame([
        ["Sunny", "Hot",  "High",   "Weak",   "No"],
        ["Sunny", "Hot",  "High",   "Strong", "No"],
        ["Overcast", "Hot", "High", "Weak",   "Yes"],
        ["Rain", "Mild", "High",    "Weak",   "Yes"],
        ["Rain", "Cool", "Normal",  "Weak",   "Yes"],
        ["Rain", "Cool", "Normal",  "Strong", "No"],
        ["Overcast", "Cool", "Normal", "Strong", "Yes"],
        ["Sunny", "Mild", "High",   "Weak",   "No"],
    ], columns=["Outlook", "Temperature", "Humidity", "Wind", "Play"])

def simple_rules(df):
    """Generate readable one-condition rules with perfect precision on this dataset."""
    target = df.columns[-1]
    features = list(df.columns[:-1])
    rules = []
    for feature in features:
        for value in df[feature].dropna().unique():
            subset = df[df[feature] == value]
            labels = subset[target].unique()
            if len(labels) == 1:
                rules.append(f"IF {feature} = {value} THEN {target} = {labels[0]}")
    return rules

def foil_gain(p0, n0, p1, n1):
    """FOIL information gain for a candidate literal."""
    import math
    if p1 == 0 or p0 == 0:
        return 0.0
    return p1 * (math.log2(p1 / (p1 + n1)) - math.log2(p0 / (p0 + n0)))

def foil_like_rules(df):
    """
    A compact FOIL-style learner for a categorical target:
    repeatedly add the attribute=value condition that best separates positive
    examples from negative examples. This is an educational simplified version,
    not a full first-order logic implementation.
    """
    target = df.columns[-1]
    positive_label = df[target].mode().iloc[0]
    positives = df[df[target] == positive_label]
    negatives = df[df[target] != positive_label]
    rules = []

    for _, example in positives.iterrows():
        conditions = []
        remaining_pos = positives.copy()
        remaining_neg = negatives.copy()
        available = list(df.columns[:-1])

        while len(remaining_neg) > 0 and available:
            best = None
            best_score = -1
            for col in available:
                value = example[col]
                p0, n0 = len(remaining_pos), len(remaining_neg)
                pos2 = remaining_pos[remaining_pos[col] == value]
                neg2 = remaining_neg[remaining_neg[col] == value]
                score = foil_gain(p0, n0, len(pos2), len(neg2))
                if len(pos2) and score > best_score:
                    best, best_score = (col, value, pos2, neg2), score
            if best is None:
                break
            col, value, remaining_pos, remaining_neg = best
            conditions.append(f"{col}={value}")
            available.remove(col)

        if conditions:
            rule = "IF " + " AND ".join(conditions) + f" THEN {target}={positive_label}"
            if rule not in rules:
                rules.append(rule)
    return rules

if __name__ == "__main__":
    df = get_data()
    print("Dataset:\n", df.to_string(index=False))
    print("\nExample-based categorical rules:")
    for rule in simple_rules(df):
        print(rule)
    print("\nFOIL-style learned rules:")
    for rule in foil_like_rules(df):
        print(rule)
