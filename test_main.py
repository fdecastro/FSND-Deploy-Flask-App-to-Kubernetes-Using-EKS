'''
Tests for jwt flask app.
'''
import os
import json
import pytest
import main

SECRET = 'd7e7b147-24c5-472c-afdd-6890dba6048e'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQxNjk0MzUsIm5iZiI6MTU5Mjk1OTgzNSwiZW1haWwiOiJmZGM1MDBAZ21haWwuY29tIn0._RHtDo7m_zAnk0G9FOUljsRApxnAolfOMVVFv5ukxJ4'
EMAIL = 'fdc500@gmail.com'
PASSWORD = '123456'


@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client


def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    # assert False


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
    # assert False
