import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report

# Inbuilt dataset: Iris (150 samples, 4 numeric features, 3 classes).
# To use a CSV instead, replace this block with pd.read_csv("your_file.csv"),
# then set X = df.drop(columns=["target"]) and y = df["target"].
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Bagging
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42
)
bagging.fit(X_train, y_train)
bag_pred = bagging.predict(X_test)

print("=== BAGGING ===")
print("Accuracy:", round(accuracy_score(y_test, bag_pred), 3))
print(classification_report(y_test, bag_pred, target_names=iris.target_names, zero_division=0))

# Boosting
boosting = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42
)
boosting.fit(X_train, y_train)
boost_pred = boosting.predict(X_test)

print("=== ADABOOST ===")
print("Accuracy:", round(accuracy_score(y_test, boost_pred), 3))
print(classification_report(y_test, boost_pred, target_names=iris.target_names, zero_division=0))
