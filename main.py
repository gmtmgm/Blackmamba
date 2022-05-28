import threading
import json

from tokenizing import Preprocess
from find_answer import *
from DB_connect import Database
from intent_model import IntentModel
from BotServer import BotServer
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#전처리 객체
p = Preprocess(userdic= './user_dic.txt')

#의도 파악 모델
intent = IntentModel(model_name= './intent_model.h5', proprocess=p)



def to_client(conn, addr, params):
    db = params['db']
    try:
        db.connect()

        read = conn.recv(2048)
        print('\n')
        print('Connection from: %s' % str(addr))

        if read is None or not read:
            print('클라이언트 연결 끊어짐')
            exit(0)

        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']

        f = FindAnswer(db)
            
        pos = p.pos(query)
        print("pos:")
        print(pos)
        keywords = p.get_keywords(pos)
        print("keyword:")
        print(keywords)
        tags = f.sort_tags(keywords)
        print(tags)
        intent_id = tags[0]
        print(intent_id)
        answer = f.answer_text(keywords)
        print(answer)


        send_json_data_str = {
            "Query" : query,
            "Answer": answer,
            "Intent": intent_id,
        }
        message = json.dumps(send_json_data_str)
        conn.send(message.encode())

    except Exception as ex:
        print(ex)

    finally:
        if db is not None: # db 연결 끊기
            db.close()
        conn.close()

if __name__ == '__main__':

    db = Database(
    host="localhost", port=1521, service_name="XE",
    user="c##Blackmamba", password="blackmamba"
    )
    print("DB 접속")
    
    # 봇 서버 동작
    port = 5050
    listen = 100
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True:
        conn, addr = bot.ready_for_client()
        params = {
            "db": db
        }

        client = threading.Thread(target=to_client, args=(
            conn,
            addr,
            params
        ))
        client.start()

