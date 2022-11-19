import ibm_db

db = "bludb"
uid = "jbq48131"
pwd = "9dfeNQz767i2KzLe"
host = "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
port = "31198"
security = "SSL"
sec = "./cert.crt"

con = 'DATABASE={};HOSTNAME={};PORT={};UID={};PWD={};SECURITY={};SSLServerCertificate={}'.format(db, host, port, uid, pwd, security, sec)
conn = ibm_db.connect(con, "", "")
print("connected")