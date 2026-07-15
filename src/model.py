import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/cleaned/cleaned_superstore.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
print("========== DATASET LOADED ==========")
print(df.head())

print("\nShape:", df.shape)

# ==========================================
# Features (X) and Target (y)
# ==========================================

X = df[
    [
        "Category",
        "Sub-Category",
        "Region",
        "Segment",
        "Ship Mode",
        "Quantity",
        "Discount",
        "Delivery Days"
    ]
]

y = df["Sales"]

print("\n========== FEATURES ==========")
print(X.head())

print("\n========== TARGET ==========")
print(y.head())

# ==========================================
# Categorical Columns
# ==========================================

categorical_columns = [
    "Category",
    "Sub-Category",
    "Region",
    "Segment",
    "Ship Mode"
]

print("\nCategorical Columns:")
print(categorical_columns)
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

encoded_data = encoder.fit_transform(X[categorical_columns])

print("\nEncoded Data Shape:")
print(encoded_data.shape)

# ==========================================
# Numerical Features
# ==========================================

numerical_columns = [
    "Quantity",
    "Discount",
    "Delivery Days"
]

numerical_data = X[numerical_columns].values

print("\nNumerical Data Shape:")
print(numerical_data.shape)

# ==========================================
# Final Feature Matrix
# ==========================================

X_final = np.hstack((encoded_data, numerical_data))

print("\nFinal Feature Matrix Shape:")
print(X_final.shape)

# ==========================================
# Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_final,
    y,
    test_size=0.2,
    random_state=42
)

print("\n========== TRAIN-TEST SPLIT ==========")

print("X_train Shape:", X_train.shape)
print("X_test Shape :", X_test.shape)

print("y_train Shape:", y_train.shape)
print("y_test Shape :", y_test.shape)

# ==========================================
# Linear Regression Model
# ==========================================

model = LinearRegression()

print("\nLinear Regression Model Created Successfully!")

# Train the model

model.fit(X_train, y_train)

print("Model Training Completed!")

print("\nNumber of Features:", len(model.coef_))
print("Intercept:", model.intercept_)
# ==========================================
# Make Predictions
# ==========================================

y_pred = model.predict(X_test)

print("\n========== PREDICTIONS ==========")
print(y_pred[:10])
comparison = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})

print("\n========== ACTUAL vs PREDICTED ==========")
print(comparison.head(10))

# ==========================================
# Mean Absolute Error (MAE)
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")
print("Mean Absolute Error (MAE):", mae)

# ==========================================
# Mean Squared Error (MSE)
# ==========================================

mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)

# ==========================================
# Root Mean Squared Error (RMSE)
# ==========================================

rmse = np.sqrt(mse)

print("Root Mean Squared Error (RMSE):", rmse)

# ==========================================
# R² Score
# ==========================================

r2 = r2_score(y_test, y_pred)

print("R² Score:", r2)

# ==========================================
# Save Trained Model
# ==========================================

joblib.dump(model, "models/sales_prediction_model.pkl")

print("\nModel saved successfully!")

# ==========================================
# Save OneHotEncoder
# ==========================================

joblib.dump(encoder, "models/onehot_encoder.pkl")

print("OneHotEncoder saved successfully!")

# ==========================================
# Decision Tree Regressor
# ==========================================

dt_model = DecisionTreeRegressor(
    random_state=42,
    max_depth=10
)

print("\nDecision Tree Model Created!")
#training
dt_model.fit(X_train, y_train)

print("Decision Tree Training Completed!")
dt_pred = dt_model.predict(X_test)

print("\nDecision Tree Predictions:")
print(dt_pred[:10])

# ==========================================
# Decision Tree Evaluation
# ==========================================

dt_mae = mean_absolute_error(y_test, dt_pred)
dt_mse = mean_squared_error(y_test, dt_pred)
dt_rmse = np.sqrt(dt_mse)
dt_r2 = r2_score(y_test, dt_pred)

print("\n========== DECISION TREE EVALUATION ==========")
print("MAE :", dt_mae)
print("MSE :", dt_mse)
print("RMSE:", dt_rmse)
print("R²  :", dt_r2)

# ==========================================
# Random Forest Regressor
# ==========================================

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

print("\nRandom Forest Model Created!")

rf_model.fit(X_train, y_train)

print("Random Forest Training Completed!")

rf_pred = rf_model.predict(X_test)

print("\nRandom Forest Predictions:")
print(rf_pred[:10])

# ==========================================
# Random Forest Evaluation
# ==========================================

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_pred)

print("\n========== RANDOM FOREST EVALUATION ==========")
print("MAE :", rf_mae)
print("MSE :", rf_mse)
print("RMSE:", rf_rmse)
print("R²  :", rf_r2)

# ==========================================
# Save Best Model
# ==========================================

import joblib

joblib.dump(model, "models/best_model.pkl")

print("\nBest Model Saved Successfully!")

# ==========================================
# Actual vs Predicted Plot
# ==========================================

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")

plt.title("Actual vs Predicted Sales")

plt.tight_layout()

plt.savefig("images/actual_vs_predicted.png")

plt.show()

# ==========================================
# Residual Error Plot
# ==========================================

residuals = y_test - y_pred

plt.figure(figsize=(8,6))

plt.scatter(
    y_pred,
    residuals,
    alpha=0.6
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.xlabel("Predicted Sales")
plt.ylabel("Residual Error")

plt.title("Residual Error Plot")

plt.tight_layout()

plt.savefig("images/residual_error_plot.png")

plt.show()

encoded_feature_names = encoder.get_feature_names_out(categorical_columns)

print("Encoded Features:", len(encoded_feature_names))
print("Numerical Features:", len(numerical_columns))
print("Total Feature Names:", len(list(encoded_feature_names) + numerical_columns))
print("Coefficients:", len(model.coef_))

encoded_feature_names = encoder.get_feature_names_out(categorical_columns)

all_feature_names = list(encoded_feature_names) + numerical_columns

print(type(all_feature_names))
print(len(all_feature_names))

print(type(model.coef_))
print(len(model.coef_))

feature_importance = pd.DataFrame()

feature_importance["Feature"] = all_feature_names
feature_importance["Coefficient"] = model.coef_

print(feature_importance.head())