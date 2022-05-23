import cx_Oracle as cx

dsn = cx.makedsn("localhost", 1521, service_name= "XE")
db = cx.connect(user="c##Blackmamba", password="blackmamba", dsn=dsn)

cur = db.cursor()
cursor = cur.execute("select * from 프랜차이즈")

for i in cursor:
    print(i)

cur.close()
db.close()
