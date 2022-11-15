from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/templates/donor')
def donor():
    return render_template('donor.html')


@app.route('/templates/adminlogin', methods=['POST', 'GET'])
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/templates/donorregister')
def donorregister():
    return render_template('donorregister.html')


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

            return render_template('list.html')


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

# @app.route('/delete/<phoneno>')
# def delete(phoneno):
#   sql = f"SELECT * FROM DONOR WHERE phoneno='{escape(phoneno)}'"
#   print(sql)
#   stmt = ibm_db.exec_immediate(conn, sql)
#   donor = ibm_db.fetch_row(stmtRE phoneno='{escape(phoneno)}'"
#     print(sql)
#     stmt = ibm_db.exec_immediate(conn, sql)

#     students = [])
#   print ("The Name is : ",  donor)
#   if student:
#     sql = f"DELETE FROM DONOR WHERE
#     sql = "SELECT * FROM DONOR"
#     stmt = ibm_db.exec_immediate(conn, sql)
#     dictionary = ibm_db.fetch_both(stmt)
#     while dictionary != False:
#       DONOR.append(dictionary)
#       dictionary = ibm_db.fetch_both(stmt)
#     if donor:
#       return render_template("list.html", students = students, msg="Delete successfully")

