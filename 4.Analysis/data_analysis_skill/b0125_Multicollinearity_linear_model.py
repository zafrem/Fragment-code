import pandas as pd
# pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error

data = {
    'Feature_1': [1, 2, 3, 4, 5],   # Feature_2 Strongly correlated variables
    'Feature_2': [2, 4, 6, 8, 10],  # Feature_1 Strongly correlated variables
    'Feature_3': [5, 3, 4, 2, 1],
    'Target': [1.1, 2.0, 3.2, 4.1, 5.3]
}
df = pd.DataFrame(data)

# Separate the independent variable (X) from the dependent variable (y)
X = df[['Feature_1', 'Feature_2', 'Feature_3']]
y = df['Target']

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge regression model training and forecasting
ridge_model = Ridge(alpha=1.0)  # alpha determines the normalization strength
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# Lasso regression model training and forecasting
lasso_model = Lasso(alpha=0.1)  # alpha determines the normalization strength
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)

# Performance evaluation (with MSE)
ridge_mse = mean_squared_error(y_test, ridge_predictions)
lasso_mse = mean_squared_error(y_test, lasso_predictions)

# 결과 출력
print("Ridge Predicted values from regression models:", ridge_predictions)
print("Ridge regression models MSE:", ridge_mse)

print("Lasso Predicted values from regression models:", lasso_predictions)
print("Lasso regression models MSE:", lasso_mse)
