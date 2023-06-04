# Product Price Distribution Analysis

This project performs an analysis of product price distribution based on a CSV file containing product versions and prices. It utilizes Python libraries such as pandas, matplotlib, and scikit-learn to read the data, visualize it with a scatter plot, and perform linear regression.

## Project Overview

- The main code file is `product_price_analysis.py`, which contains the code for reading the CSV file, visualizing the data, performing linear regression, and predicting prices.
- The CSV file (`product_price.csv`) contains two columns: `product_version` and `price`. It provides the necessary data for analyzing the relationship between product versions and their prices.
- The analysis begins by reading the CSV file using pandas, followed by visualizing the data using matplotlib to gain insights into the distribution of product prices based on their versions.
- Linear regression is then performed using scikit-learn's LinearRegression class to estimate a linear relationship between the product version and its corresponding price.
- Finally, the code predicts the price for a specific product version, demonstrating the predictive capability of the trained linear regression model.

## Getting Started

1. Clone the repository or download the code files.
2. Ensure that Python 3 and the required libraries (pandas, matplotlib, scikit-learn) are installed in your environment.
3. Place the CSV file (`product_price.csv`) containing the product version and price data in the same directory as the code files.

## Usage

1. Run the `product_price_analysis.py` script using a Python interpreter.
2. The script will read the CSV file, visualize the data using a scatter plot, and display the plot.
3. The linear regression model is then trained on the data, allowing for price predictions for specific product versions.
4. Modify the code to use different CSV files or customize the analysis as per your requirements.

## Results

- The scatter plot visualizes the product price distribution, providing insights into the relationship between product versions and prices.
- The linear regression model estimates a linear relationship between the product version and its price, enabling price predictions for unseen product versions.


## Acknowledgments

The project makes use of the following Python libraries:

- pandas: [https://pandas.pydata.org/](https://pandas.pydata.org/)
- matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
- scikit-learn: [https://scikit-learn.org/](https://scikit-learn.org/)

Special thanks to the authors and contributors of these libraries for their valuable work.

