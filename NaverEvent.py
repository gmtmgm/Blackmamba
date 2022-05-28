import requests, json
import cx_Oracle as cx
import intent_model
import find_answer

dsn = cx.makedsn("localhost", 1521, service_name= "XE")
db = cx.connect(user="c##Blackmamba", password="blackmamba", dsn=dsn)
cur = db.cursor()

class NaverEvent:
    def __init__(self, authorization):
        self.authorization_key = authorization

    def textContentComponent(self, text):
        return {
            "textContent": {
                "text": text
            }
        }

    def send_message(self, user_key, component):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': self.authorization_key,
        }

        if component == 1:
            f_list = []
            f_list.append(db.exedata('''SELECT 이름 FROM 프랜차이즈'''))
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": cur.answer_text(component, a_tags="프랜차이즈"),"buttonList": [ '
            datatext = data_fr1+data_fr2
            data_ex1 = []
            inte1, inte2 = 0
            for text1 in f_list:
                data_ex1[inte1] = '{"type": "TEXT","data": {"title": "%s","code": "코드"}},' % text1
                inte1=inte1+1
            data_ex2 = ''' ]}]}} '''
            for text2 in data_ex1:
                datatext=datatext+data_ex1[inte2]
                inte2 = inte2 + 1
            datatext=datatext.rstip+data_ex2
            data = json.loads(datatext)

        data.update(component)

        message = json.dumps(data)
        return requests.post(
            'https://gw.talk.naver.com/chatbot/v1/event',
            headers=headers,
            data=message
        )

    def send_resp(self, dst_user_key, bot_resp):
        if bot_resp['Answer'] is not None:
            text = self.textContentComponent(bot_resp['Answer'])
            self.send_message(user_key=dst_user_key, component=text)

        return json.dumps({}), 200
