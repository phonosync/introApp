# Python Flask App for Linear Regression
Author:
Exposes endpoints to train a linear regression model and predict based on the trained model

# 

# Requirements and Setup
* Python 3.7+
* pip install -r requirements.txt
* create environment variables configuration file `.env` in project root based on `.env.template`

# Run the app
Execute from project root: `python app.py`

# Tests
Execute from project root:
* `pycodestyle --exclude=venv`
* pytest tests\test_linreg.py
* integration:
    * start the app first: `python app.py`
    * `pytest tests\requests.py`