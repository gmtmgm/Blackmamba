from flask import Flask, request, jsonify, abort
import socket
import json

host = "127.0.0.1"
port = 5050

app = Flask(__name__)


def get_answer_from_engine(bottype, query):
    mySocket = socket.socket()
    mySocket.connect((host, port))

    json_data = {
        'Query': query,
        'Bottype': bottype
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
            skillTemplaate = KakaoTemplate()
            return skillTemplaate.send_resp(ret)

        elif bot_type == "NAVER":
            body = request.get_json()
            user_key = body['user']
            event = body['event']

            from NaverEvent import NaverEvent
            authorization_key = '<보내기 API 인증키>'
            naverEvent = NaverEvent(authorization_key)

            if event == "open":
                print("알레르기 유발물질을 알려주는 챗봇, 알보입니다. 무엇을 도와드릴까요?")
                return json.dumps({}), 200
            elif event == "leave":
                print("이용해주셔서 감사합니다.")
                return json.dumps({}), 200

            elif event == "send":
                user_text = body['textContent']['text']
                ret = get_answer_from_engine(bottype=bot_type, query=user_text)
                return naverEvent.send_response(user_key)
        else:
            abort(404)

    except Exception as ex:
        abort(500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
