
import cx_Oracle as cx

class Database:

    def __init__(self, host, port, service_name, user, password):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.user = user
        self.password = password
        self.conn = None
    
    def connect(self):
        if self.conn != None:
            return
        self.conn = cx.connect(
            user=self.user,
            password=self.password,
            dsn=cx.makedsn(self.host, self.port, self.service_name)
        )
    
    def close(self):
        if self.conn is None:
            return 
        self.conn.close()
        self.conn = None
    
    def exedata(self, sql):
        data = []
        cur = self.conn.cursor()
        cursor = cur.execute(sql)
        for i in cursor:
            for ii in i:
                data.append(ii)
        cur.close()
        return data


db = Database(
    host="localhost", port=1521, service_name="XE", 
    user="c##Blackmamba", password="blackmamba"
)

"""
테스트
db.connect()

sql = "select * from 프랜차이즈"
print(db.exedata(sql))
db.close()
"""
