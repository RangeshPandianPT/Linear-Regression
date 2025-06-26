import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("Housing_modified.csv")
X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

plt.figure(figsize=(8, 5))
plt.scatter(X_test["area"], y_test, color="blue", label="Actual")
plt.scatter(X_test["area"], y_pred, color="red", label="Predicted")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Actual vs Predicted Price")
plt.legend()
plt.grid(True)
plt.savefig("regression_plot.png")
plt.show()