import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv("price.csv")

# 🔹 Convert yes/no to 0/1 (if your dataset has yes/no)
data["sex"] = data["sex"].map({"male": 1, "female": 0})
data["smoker"] = data["smoker"].map({"yes": 1, "no": 0})
data["children"] = data["children"].map({"yes": 1, "no": 0})

# 🔹 One-hot encode region
data = pd.get_dummies(data, columns=["region"], drop_first=True)

# 🔹 Features and target
X = data.drop("charges", axis=1)
y = data["charges"]

# 🔹 Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 🔹 Save column names (VERY IMPORTANT)
joblib.dump(model, "model_columns.pkl")

print("✅ Model trained and saved successfully!")