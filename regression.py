
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

# # ================================
# # ✅ 1️⃣ Simple Linear Regression
# # ================================

# x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# y = np.array([2, 4, 5, 4, 5])

# model1 = LinearRegression()
# model1.fit(x, y)
# y_pred = model1.predict(x)

# plt.scatter(x, y, color="darkgreen", label="Actual")
# plt.plot(x, y_pred, color="blue", linewidth=2, label="Regression Line")
# plt.title("Simple Linear Regression")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.legend()
# plt.show()

# print("\n🔹 Simple Linear Regression Summary")
# print("Coefficient (Slope):", model1.coef_[0])
# print("Intercept:", model1.intercept_)
# print("R² Score:", r2_score(y, y_pred))



# # ===================================
# # ✅ 2️⃣ Multiple Linear Regression
# # ===================================

# x1 = np.array([1, 2, 3, 4, 5])
# x2 = np.array([2, 1, 3, 5, 4])
# y = np.array([5, 6, 7, 10, 11])

# X = np.column_stack((x1, x2))  # Combine predictors

# model2 = LinearRegression()
# model2.fit(X, y)
# y_pred2 = model2.predict(X)

# plt.scatter(y, y_pred2, color="purple")
# plt.plot([min(y), max(y)], [min(y), max(y)], color="red", linewidth=2)
# plt.title("Multiple Linear Regression: Observed vs Predicted")
# plt.xlabel("Observed Y")
# plt.ylabel("Predicted Y")
# plt.show()

# print("\n🔹 Multiple Linear Regression Summary")
# print("Coefficients:", model2.coef_)
# print("Intercept:", model2.intercept_)
# print("R² Score:", r2_score(y, y_pred2))



# # ===================================
# # ✅ 3️⃣ Logistic Regression
# # ===================================

x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])

model3 = LogisticRegression()
model3.fit(x, y)
prob = model3.predict_proba(x)[:, 1]  # Predicted probabilities

plt.scatter(x, y, color="darkgreen", label="Actual")
plt.plot(x, prob, color="red", linewidth=2, label="Logistic Curve")
plt.title("Logistic Regression")
plt.xlabel("X values")
plt.ylabel("Probability")
plt.legend()
plt.show()

y_pred3 = model3.predict(x)
print("\n🔹 Logistic Regression Summary")
print("Coefficients:", model3.coef_)
print("Intercept:", model3.intercept_)
print("Accuracy:", accuracy_score(y, y_pred3))
