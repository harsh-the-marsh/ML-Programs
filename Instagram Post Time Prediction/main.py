import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime

# Load data from CSV file
data = pd.read_csv('instagram_data.csv')

# Split data into training and testing sets
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train linear regression model on the training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the best time to post
new_post = [[datetime.datetime.today().weekday(), 500, 50, 10]]
prediction = regressor.predict(new_post)
print("The best time to post is on", datetime.datetime.fromtimestamp(prediction[0]).strftime('%A %I:%M %p'))