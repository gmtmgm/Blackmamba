import cx_Oracle as cx
conn = cx.connect("c##Blackmamba", "blackmamba", "203.255.63.28:1512/xe")

cur = conn.cursor()
cur.execute("select * from 프랜차이즈;")


for i in cursor:
    print(i)

cur.close()
conn.close()
