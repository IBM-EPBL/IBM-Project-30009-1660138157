from flask import Flask, request
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()
from turtle import st 

from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

from utils.request import validate_body
from utils.response import response, error_response
from utils.sms import send_bulk_sms

import ibm_db

db = "bludb"
uid = "jbq48131"
pwd = "9dfeNQz767i2KzLe"
host = "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
port = "31198"
security = "SSL"
sec = "./cert.crt"

con = 'DATABASE={};HOSTNAME={};PORT={};UID={};PWD={};SECURITY={};SSLServerCertificate={}'.format(
    db, host, port, uid, pwd, security, sec)
conn = ibm_db.connect(con, "", "")

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/templates/donor')
def donor():

#     if(request.method == 'POST'):
#         sql = "SELECT EMAIL , PASSWORD FROM DONOR WHERE phoneno=?"
#         stmt = ibm_db.prepare(conn, sql)
#         ibm_db.bind_param(stmt, 5, phoneno)
#         ibm_db.execute(stmt)
#         account = ibm_db.fetch_both(stmt)
#         while account != False:
#             Email =account[1]
#             Password = account[2]
#             break
    return render_template('donor.html')


@app.route('/templates/adminlogin', methods=['POST', 'GET'])
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/templates/donorregister')
def donorregister():
    return render_template('donorregister.html')

@app.route('/templates/dhome')
def dhome():
    return render_template("dhome.html")


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    # if(request.method == 'GET'):
    #   return render_template('donorregister.html')

    if (request.method == 'POST'):

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        phoneno = request.form['phoneno']
        dob = request.form['dob']
        bloodgroup = request.form['bloodgroup']
        gender = request.form['gender']
        city = request.form['city']
        pin = request.form['pin']
        address = request.form['address']


        sql = "SELECT * FROM DONOR WHERE phoneno={}".format(phoneno)
        stmt = ibm_db.prepare(conn, sql)
        # ibm_db.bind_param(stmt, 5, phoneno)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if (account):
            return render_template('donor.html')

        else:
            insert_sql = "INSERT INTO DONOR VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.bind_param(prep_stmt, 4, confirm)
            ibm_db.bind_param(prep_stmt, 5, phoneno)
            ibm_db.bind_param(prep_stmt, 6, dob)
            ibm_db.bind_param(prep_stmt, 7, bloodgroup)
            ibm_db.bind_param(prep_stmt, 8, gender)
            ibm_db.bind_param(prep_stmt, 9, city)
            ibm_db.bind_param(prep_stmt, 10, pin)
            ibm_db.bind_param(prep_stmt, 11, address)
            ibm_db.execute(prep_stmt)

            return render_template('donor.html')


@app.route('/templates/list')
def list():
    donor = []
    sql = "SELECT * FROM DONOR"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)

    while dictionary != False:
    #    print ("The Name is : ",  dictionary)
       donor.append(dictionary)
       dictionary = ibm_db.fetch_both(stmt)

    return render_template("list.html", DONOR=donor)

@app.route('/templates/sms')
def sms():
    return render_template("sms.html")



@app.route('/message', methods=['POST'])
def message_aud():
      sql="SELECT*FROM DONOR WHERE PHONENO=?"
      body = request.get_json()
      status, missing_field = validate_body(body, ['message', 'sql'])
      if not status:
            return error_response(f'{missing_field} is missing')
      send_bulk_sms(body['sql'], body['message'])
      return response(True, 'Success', None)


@app.route('/templates/sent')
def sent():
    return render_template("sent.html")



if __name__ == '__main__':
    app.run()





