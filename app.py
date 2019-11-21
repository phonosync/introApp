import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.app_resources import Train
from src.app_resources import Predict
from src.app_resources import Base
from dotenv import load_dotenv
load_dotenv()                                   # Load Runtime configuration


app = Flask(__name__)                           #  Create a Flask WSGI application
api = Api(app)                                  #  Create a Flask-RESTful API
CORS(app)
api = Api(app)


# The resource classes are defined in a separate module: src.app_resources
api.add_resource(Base, '/')                     #  Create a URL route to the first resource

api.add_resource(Train, '/train')

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    host = os.getenv('APP_HOST')
    port = os.getenv('APP_PORT')                # Here we are using the runtime configuration
    app.run(debug=True, host=host, port=port)   #  Start a development server
