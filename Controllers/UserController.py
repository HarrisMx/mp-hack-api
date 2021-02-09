import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'DBF'))
from DBConnect import Database
from flask import jsonify

class UserController(object):
    def __init__(self):
        pass
    
    @staticmethod
    def connect_db():
        try:
            dbconn = Database.connect()
            return dbconn
        except Exception as e:
            return jsonify({"ConnectionError": str(e)})

    @staticmethod
    def addUser(request):
        try:
            dbconn = UserController.connect_db()
            return jsonify({"Message": "User Added", "Success": True})
        except Exception as exc:
            return jsonify({"AddUserError": str(exc)})
    
    @staticmethod
    def updateUser(request):
        try:
            pass
        except Exception as exc:
            return jsonify({"UpdateUserError": str(exc)})