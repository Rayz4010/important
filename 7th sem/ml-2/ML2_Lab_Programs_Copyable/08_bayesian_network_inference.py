# Install first: pip install pgmpy pandas
import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

USE_CSV = False
CSV_PATH = "weather_traffic.csv"

def get_data():
    if USE_CSV:
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame({
        "Rain":    ["Yes", "Yes", "No", "No", "Yes", "No", "Yes", "No", "Yes", "No"],
        "Traffic": ["Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No", "Yes", "No"],
        "Late":    ["Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No", "Yes", "No"],
    })

data = get_data()
model = DiscreteBayesianNetwork([
    ("Rain", "Traffic"),
    ("Traffic", "Late"),
    ("Rain", "Late")
])
model.fit(data, estimator=MaximumLikelihoodEstimator)
inference = VariableElimination(model)

print("1. P(Late | Rain=Yes)")
print(inference.query(variables=["Late"], evidence={"Rain": "Yes"}))

print("\n2. P(Rain | Late=Yes)")
print(inference.query(variables=["Rain"], evidence={"Late": "Yes"}))

print("\n3. P(Late | Traffic=Yes, Rain=No)")
print(inference.query(
    variables=["Late"],
    evidence={"Traffic": "Yes", "Rain": "No"}
))
