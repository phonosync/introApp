import os
import requests
from dotenv import load_dotenv
load_dotenv()


def test_base():
    url = 'http://' + str(os.getenv('APP_HOST')) + ':' + str(os.getenv('APP_PORT'))
    response = requests.get(url)
    body = response.json()

    assert response.status_code == 200
    assert body['status'] == 'ok'


def test_train():
    url = 'http://' + str(os.getenv('APP_HOST')) + ':' + str(os.getenv('APP_PORT')) + '/train'
    payload = {'x': [[1], [2], [3]],
               'y': [1.0, 2.0, 3.0]}

    response = requests.post(url, json=payload)
    assert response.status_code == 200


def test_predict():
    url = 'http://' + str(os.getenv('APP_HOST')) + ':' + str(os.getenv('APP_PORT')) + '/predict'
    payload = {'x': [[1.0]]}
    response = requests.post(url, json=payload)
    assert response.status_code == 200


if __name__ == '__main__':
    test_predict()
