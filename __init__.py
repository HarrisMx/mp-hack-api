#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'Controllers'))
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from flask_accept import accept
from UserController import UserController
# from flask_socketio import SocketIO
import os
import json
from datetime import date, datetime
#from pyfcm import FCMNotification

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'mzwakhe':
        return 'a9794af4-7773-4a9b-8e25-4dc2ca2a6781'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

def not_found(error):
    return make_response(jsonify( { 'error': 'Not Found' } ), 404)

@app.route('/api/v1/', methods=['POST'])
def Root():
    try:
        res = UserController.addUser(request)
        return res
    except Exception as exc:
        return make_response(jsonify({"Error": str(exc)}))

@app.route('/api/v1/Login', methods=['POST'])
def Login():
    try:
        if not request.json or not 'password' in request.json:
            abort(400)
        res = UserController.LoginUser(request)
        return res
    except Exception as exc:
        return make_response(jsonify({"LoginError": str(exc)}))

@app.route('/api/v1/dataUpload', methods=['POST'])
def wasteImage():
    try:
        pass
    except Exception as exc:
        return make_response(jsonify({"uploadError": str(exc)}))

if __name__ == '__main__':
    app.run(debug=True, port=5241)