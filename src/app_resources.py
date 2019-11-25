import os
from flask_restful import Resource
from flask import request
from flask import current_app as app
from src import linreg

model_path = os.path.join('model', 'linreg.joblib')


class Base(Resource):                           #  Create a RESTful resource
    def get(self):                              #  Create GET endpoint
        return {'status': 'ok'}


class Train(Resource):
    """
    Train and store a new linear regression model
    """

    def post(self):
        app.logger.info("Received post to train")
        try:
            req_body = request.get_json()
        except Exception as e:
            msg = "Failed to to extract request body"
            app.logger.exception(msg)
            app.logger.exception(e)
            return {'error': msg}, 400

        try:
            x_train = req_body['x']
            y_train = req_body['y']
            assert len(x_train) == len(y_train)
        except KeyError:
            msg = "Failed to extract training data from request body"
            app.logger.exception(msg)
            return {'error': msg}, 400
        except AssertionError:
            msg = 'Training data x and y not equal length'
            app.logger.exception(msg)
            return {'error': msg}, 400

        app.logger.info("Attempting to fit model")
        try:
            new_model = linreg.fit_model(x_train, y_train)
        except Exception as e:
            app.logger.exception("Failed to fit model")
            app.logger.exception(e)
            return {'error': 'Failed to fit model'}, 500

        app.logger.info("Training completed. Attempting to store model")
        try:
            linreg.store_model(new_model, model_path)
        except Exception as e:
            app.logger.exception(e)
            return {'error': 'Failed to store new model'}, 500
        app.logger.info("Successfully stored new model.")
        return {'status': 'ok'}


class Predict(Resource):
    """
    Predict with trained model
    """
    def post(self):
        try:
            req_body = request.get_json()
        except Exception as e:
            app.logger.exception("Failed to to extract request body")
            return {'error': 'Failed to train'}, 400

        try:
            x = req_body['x']
            assert len(x) > 0
        except KeyError:
            msg = "Expected {'x': <array-like object with more than 0 elements>}"
            app.logger.exception(msg)
            return {'error': msg}, 400

        try:
            m = linreg.load_model(model_path)
        except Exception as e:
            msg = 'failed to load model'
            app.logger.exception(msg)
            return {'error': msg}, 500

        try:
            pred = linreg.predict_model(m, x)
        except Exception as e:
            app.logger.exception(e)
            return {'error': 'Prediction failed'}, 500

        return {'status': 'ok', 'y': pred.tolist()}
