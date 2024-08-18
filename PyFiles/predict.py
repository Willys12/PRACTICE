#!/usr/env python3

import numpy as np
from sklearn.linear_model import LinearRegression

def train_model(data):
    """
    Trains a linear model using the data provided.
    """
    x = data[:, 1].reshape(-1, 1)
    y = data[:, 2]

    model = LinearRegression()
    model.fit(x, y)
    return model

def predict_liverpool_points(model, arsenal_points):
    """_summary_
    Predict Liverpool's based on Arsenal's points using the trained model
    """

    return model.predict([[arsenal_points]])[0]
if __name__ == "__main__":
    data = np.array([[1, 68, 70], [2, 70, 72], [3, 72, 74]])

    model = train_model(data)

    arsenal_points = 68
    liverpool_points = predict_liverpool_points(model, arsenal_points)
    print(f"Predicted Liverpool points: {liverpool_points}")
