# Python Flask App for Linear Regression
Author: Manuel Dömer

Exposes endpoints to train a linear regression model and predict based on the trained model

# Code Organisation
```
root folder  
|-- model: Folder to store the latest model
    |--.gitkeep: Trick to commit empty folder to git
|-- src
    |-- app_resources.py: Definition of the Restful ressources and endpoints
    |-- linreg.py
        * train scikit-learn linear regression model and store it in model/linreg.joblib
        * load a trained model from model/linreg.joblib and predict for sample data
|-- tests
    |-- data: contains ressources for tests
    |-- test_linreg.py: unit tests for linre.py
    |-- test_requests.py: integration tests. Sends http requests to running Flask app
|-- app.py: the app
|-- .env: the environment variables for runtime configuration
|-- .env.template
|-- .gitignore
|-- setup.cfg: configuration for pycodestyle
|-- requirements.txt: python packages to install
|-- README.md
|-- LICENSE.md
```

# Requirements and Setup
* Python 3.7+
* pip install -r requirements.txt
* create environment variables configuration file `.env` in project root based on `.env.template`

# Run the app
* Execute from project root: `python app.py`
* Sample requests:
    * POST localhost:5000/train  payload={'x': [[1], [2], [3]],'y': [1.0, 2.0, 3.0]}
    * POST localhost:5000/predict payload={'x': [[1.0]]}

# Tests
Execute from project root:
* `pycodestyle --exclude=venv`
* pytest tests\test_linreg.py
* integration:
    * start the app first: `python app.py`
    * `pytest tests\test_requests.py`