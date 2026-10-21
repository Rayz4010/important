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
    # Inbuilt data: categorical values must match the query evidence below.
    return pd.DataFrame({
        "Rain":    ["Yes", "Yes", "No", "No", "Yes", "No", "Yes", "No", "Yes", "No"],
        "Traffic": ["Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No", "Yes", "No"],
        "Late":    ["Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No", "Yes", "No"],
    })

data = get_data()
print("Dataset:\n", data.to_string(index=False))

# Rain influences Traffic and Late; Traffic also influences Late.
model = DiscreteBayesianNetwork([
    ("Rain", "Traffic"),
    ("Traffic", "Late"),
    ("Rain", "Late")
])
model.fit(data, estimator=MaximumLikelihoodEstimator)

inference = VariableElimination(model)
result = inference.query(variables=["Late"], evidence={"Rain": "Yes"})
print("\nProbability distribution of Late given Rain=Yes:")
print(result)
