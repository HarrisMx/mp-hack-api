from config import config
import pymysql as pm

class Database(object):
    user = config['dbuser']
    password = config['bdpass']
    host = config['dbhost']
    dbname = config['dbname']
    conn = None
    _query_execute = None

    def __init__(self):
        pass
    
    @staticmethod
    def connect():
        try:
            conn = pm.connect(user=Database.user, password=Database.password, host=Database.host, db=Database.dbname)
            conn.autocommit(True)
            _query_execute = conn.cursor()
            if _query_execute:
                print("Database Connection Successful")
            return _query_execute
        except Exception as exception:
            return print("Exception caught", exception)