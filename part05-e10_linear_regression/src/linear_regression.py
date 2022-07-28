#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    #x = x[:np.newaxis] or

    # [1,2,3] ->  [1,
    #              2,
    #              3]
    #x = x[:None]
    x = x[:,np.newaxis]
    # Load the LR model
    model = LinearRegression(fit_intercept = True)

    model.fit(x,y)

    xfit = np.linspace(0,10,20)[:,None]
    yfit = model.predict(xfit)

    return model.coef_[0],model.intercept_
    
def main():

    n = 20
    x = np.linspace(0, 10, n)
    y = x**2 + 2 * np.random.randn(n)
    slope, intercept = fit_line(x,y)
    print(f"Slope: {slope}\nIntercept: {intercept}")
    
    # Define the line
    yfit = slope*x + intercept
    # Plot the coordinate system
    plt.plot(x, y, 'o')
    # Plot the line
    plt.plot(x, yfit)
    plt.show()

if __name__ == "__main__":
    main()
