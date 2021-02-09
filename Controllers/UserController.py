import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'DBF'))
from DBConnect import Database
from flask import jsonify
import hashlib
import base64

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
    
    @staticmethod
    def getUploadedData(request):
        try:
            dbconn = UserController.connect_db()
            base64Data = request.json['rpt_image_attributes']
            filename = request.json['rpt_file_name']
            UserController.SaveBase64(base64Data, filename)

            rpt_user = request.json['rpt_user']
            rpt_municipality = request.json['rpt_municipality']
            rpt_notes = request.json['rpt_notes']
            rpt_status = request.json['rpt_status']
            rpt_image_attributes = request.json['rpt_file_name']

            qry = f"INSERT INTO reports (rpt_user, rpt_municipality, rpt_notes,rpt_image_attributes, rpt_status) VALUES ('{rpt_user}', '{rpt_municipality}', '{rpt_notes}', '{rpt_image_attributes}', '{rpt_status}')"
            dbconn.execute(qry)
            return jsonify({"Message":"Data Uploaded", "Success": True})

        except Exception as exc:
            return jsonify({"UploadError": str(exc)})

    @staticmethod
    def SaveBase64(encodedData, filename):
        try:
            file_decoded = base64.b64decode(encodedData)
            path_to_save = os.path.join(os.getcwd(), 'media', 'images', filename)
            with open(path_to_save, mode='wb') as f:
                f.write(file_decoded)
        except Exception as exc:
            return jsonify({"FileError": str(exc)})

    @staticmethod
    def LoginUser(request):
        try:
            dbconn = UserController.connect_db()
            password = hashlib.md5(request.json['password'].encode())
            #print(f"Password {password.hexdigest()}")
            dbconn.execute("""SELECT per_id, per_type, per_name, acc_id, acc_logged_in, acc_pass, em_address
                        FROM accounts,emails,persons
                        WHERE em_person = per_id
                        AND acc_per_id = per_id and per_status = "A"
                        AND per_create_date < now() AND per_end_date > now() and acc_status = "A"
                        AND acc_create_date < now() AND acc_end_date > now() and em_address = '%s' and acc_pass = '%s';""" % (request.json['username'],password.hexdigest()))
            rows = dbconn.fetchall()

            
            #rows = rows[0]

            #print(f"DB Response {rows}")
            login = None
            if not rows:
                login = {'per_id':0,'per_type': ' ','per_name':' ', 'acc_logged_in': ' ', 'acc_pass': ' ', 'em_address': ' '}
            else:
                for row in rows:
                    dbconn.execute(f"UPDATE accounts SET acc_logged_in=001 WHERE acc_id='{row[0]}'")
                    #dbconn.commit()
                    login = {
                        'per_id': row[0],
                        'per_type': '%s' % row[1],
                        'per_name': '%s' % row[2],
                        'acc_logged_in': '%s' % row[3],
                        'acc_pass': '%s' % row[5],
                        'em_address':'%s' % row[6]
                    }
            dbconn.close()
            return login
        except Exception as exc:
            return jsonify({"LoginError": str(exc)})