import os
import numpy as np
from src import linreg
from dotenv import load_dotenv
load_dotenv()


def test_fit_model():
    x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(x, np.array([1, 2])) + 3
    m = linreg.fit_model(x, y)
    np.testing.assert_almost_equal(m.coef_, np.array([1., 2.]))


def test_predict_model():
    m_path = os.path.join('tests', 'data', 'linreg.joblib')
    m = linreg.load_model(m_path)
    np.testing.assert_almost_equal(m.coef_, np.array([1., 2.]))

    x_test = np.array([[3, 5]])
    y_expected = np.array([16.0])
    pred = linreg.predict_model(m, x_test)
    np.testing.assert_almost_equal(pred, y_expected)
