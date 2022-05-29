from flask import Flask, request, jsonify, abort
import socket
import json
import cx_Oracle as cx

host = "127.0.0.1"
port = 5050

app = Flask(__name__)

dsn = cx.makedsn("localhost", 1521, service_name= "XE")
db = cx.connect(user="c##Blackmamba", password="blackmamba", dsn=dsn)
cur = db.cursor()

def get_answer_from_engine(bottype, query):
    mySocket = socket.socket()
    mySocket.connect((host, port))

    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    mySocket.close()

    return ret_data


@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
    body = request.get_json()

    try:
        if bot_type == 'Test':

            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)

        elif bot_type == "KAKAO":
            body = request.get_json()
            utterance = body['userRequest']['utterance']
            ret = get_answer_from_engine(bottype=bot_type, query=utterance)

            from KakaoTemplate import KakaoTemplate
            skillTemplate = KakaoTemplate()
            return skillTemplate.send_resp(ret)

        elif bot_type == "NAVER":
            body = request.get_json()
            user_key = body['user']
            event = body['event']

            from NaverEvent import NaverEvent
            authorization_key = '<보내기 API 인증키>'
            naverEvent = NaverEvent(authorization_key)

            if event == "open":
                naverEvent.send_response(user_key, 0)
                return json.dumps({}), 200
            
            elif event == "send":
                user_text = body['textContent']['text']
                ret = get_answer_from_engine(bottype=bot_type, query=user_text)
                return naverEvent.send_response(user_key, ret)
        else:
            abort(404)

    except Exception as ex:
        abort(500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
