import os
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib


def store_model(model, m_path):
    """
    Store model to m_path
    :param model:
    :param m_path:
    :return:
    """
    joblib.dump(model, m_path)


def load_model(m_path):
    """
    Load model from path
    :param m_path:
    :return:
    """
    return joblib.load(m_path)


def fit_model(X, y):
    """
    Fit a linear regression model
    :param X: Training data
    :param y: arget values
    :return: trained model
    :rtype: sklearn.linear_model.LinearRegression
    """
    reg = LinearRegression().fit(X, y)
    return reg


def predict_model(model, X):
    """
    Predict using the input model and samples
    :param model: linear regression model
    :type model:  sklearn estimator
    :param X: Samples
    :type X: 2D array like object
    :return: Predicted values
    :rtype: array, shape(len(X))
    """
    return model.predict(np.array(X))


if __name__ == '__main__':
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([1, 2])) + 3
    print(y)
    m = fit_model(X, y)
    print(m.coef_)
    model_path = os.path.join('linreg.joblib')  # os.path.join('tests', 'data', 'linreg.joblib')
    store_model(m, model_path)
