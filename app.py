""""
Main application file.
Runs the Flask app and return mocks for every call.
"""

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from reader.reader import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})


class ApiMock(Resource):

    # Get method of /api route
    @staticmethod
    def get():
        return read('GET')

    # POST method of /api route
    @staticmethod
    def post():
        return read('POST')

    # PUT method of /api route
    @staticmethod
    def put():
        return read('PUT')

    # DELETE method of /api route
    @staticmethod
    def delete():
        return read('DELETE')


# Bind mock class to /api route
api.add_resource(ApiMock, '/api')

if __name__ == '__main__':
    app.run()





