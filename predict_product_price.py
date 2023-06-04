import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Reading the CSV file containing product version and prices
data = pd.read_csv('product_price.csv')

# Visualizing the data
plt.scatter(data['product_version'], data['price'])
plt.xlabel('Product Version')
plt.ylabel('Price')
plt.title('Product Price Distribution')
plt.show()

# Performing linear regression
model = LinearRegression()
model.fit(data[['product_version']], data[['price']])

# Predicting the price for a specific product version
prediction = model.predict([[30]])
print('Predicted price:', prediction[0][0])
