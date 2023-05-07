import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('player_data.csv', usecols=['balls', 'total_score'])

# Split the data into features and target
X = data.drop('total_score', axis=1)
y = data['total_score']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

# Make a prediction for a new match
new_data = pd.DataFrame({'balls': [50]})
new_score = model.predict(new_data)
print('Predicted score:', new_score)
