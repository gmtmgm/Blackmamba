import requests, json
import cx_Oracle as cx
import intent_model
import find_answer


class KakaoTemplate:
    def __init__(self):
        self.version = "2.0"

dsn = cx.makedsn("localhost", 1521, service_name= "XE")
db = cx.connect(user="c##Blackmamba", password="blackmamba", dsn=dsn)
cur = db.cursor()
a_filter = False
a_list = []

def simpleTextComponent(Self,text):
    return {
        "simpleText": {"text": text}
    }

def send_response(self,bot_resp):
    if bot_resp == 0:
        responseBody = {
            "version": self.version,
            "template":{
                "outputs": [
                    {
                        "basicCard": {
                            "description": cur.answer_text(bot_resp),
                            "thumbnail": {
                                "imageUrl": "chatbot_image.jpg"
                            },
                            "buttons": [
                                {
                                    "action": "프랜차이즈 보기",
                                    "label": "열어보기",
                                    "messageText": "프랜차이즈 보기"
                                }
                            ]
                        }
                    }
                ]
            }
        }

    if bot_resp == 1:
        f_list = []
        f_list.append(db.exedata('''SELECT 이름 FROM 프랜차이즈'''))
        data_fr1 = '{"version": self.version,"template":'
        data_fr2 = '{"outputs": [{"basicCard": {"description": cur.answer_text(bot_resp)}'
        data_fr3 = ',"buttons": [{"action": self.send_response(0),"label": "이전으로","messageText": "이전으로"}]}}]},'
        data_fr4 = '"quickReplies": ['
        data_ex1 = []
        for text1 in f_list:
            data_ex1.append('{"messageText": "%s","action": "message","label": "%s"},' % text1, text1)
        datatext = data_fr1+data_fr2+data_fr3+data_fr4
        for text2 in data_ex1:
            datatext = datatext+text2
        size = len(datatext)
        datatext =  datatext[:size - 1]
        data_ex2 = ']}'
        datatext = datatext+data_ex2
        responseBody = json.loads(datatext)

    if bot_resp == 2:
        m_list = []
        m_list = db.menu_find("프랜차이즈 이름", a_filter, a_list)
        data_fr1 = '{"version": self.version,"template":'
        data_fr2 = '{"outputs": [{"basicCard": {"description": cur.answer_text(bot_resp)}'
        data_fr3 = ',"buttons": [{"action": self.send_response(1),"label": "이전으로","messageText": "이전으로"},'
        data_fr4 = '{"action": self.send_response(0),"label": "처음으로","messageText": "처음으로"}]}}]},"quickReplies": ['
        data_ex1 = []
        for text1 in m_list:
            data_ex1.append('{"messageText": "%s","action": "message","label": "%s"},' % text1, text1)
        datatext = data_fr1 + data_fr2 + data_fr3 + data_fr4
        for text2 in data_ex1:
            datatext = datatext + text2
        size = len(datatext)
        datatext = datatext[:size - 1]
        data_ex2 = ']}'
        datatext = datatext + data_ex2
        responseBody = json.loads(datatext)

    if bot_resp == 3:
        a_list_in_menu = []
        a_list_in_menu = db.allergy_find("메뉴 이름")
        data_fr1 = '{"version": self.version,"template": {"outputs": [{"basicCard":'
        data_fr2 = '{"description": cur.answer_text(bot_resp, a_tags="메뉴 이름")'
        data_ma = []
        for text1 in a_list_in_menu:
            data_ma.append('"%s"' % text1)
        datatext = data_fr1+data_fr2
        for text2 in data_ma:
            datatext = datatext + text2
        size = len(datatext)
        datatext = datatext[:size - 1]
        data_ex1 = ',"thumbnail": {"imageUrl": "chatbot_image.jpg"},"buttons": '
        data_ex2 = ' [{"action": self.send_response(2),"label": "이전으로","messageText": "이전으로"},'
        data_ex3 = '{"action": self.send_response(0),"label": "처음으로","messageText": "처음으로"}]}}]}}'
        datatext = datatext + data_ex1+data_ex2+data_ex3
        responseBody = json.loads(datatext)

    if bot_resp == 4:
        allergy = db.search("알레르기 이름", a_filter, a_list)
        data_fr1 = '{"version": self.version,"template": {"outputs": [{"basicCard":'
        data_fr2 = '{"description": cur.answer_text(bot_resp, a_tags="%s")' % allergy
        data_ex1 = ',"thumbnail": {"imageUrl": "chatbot_image.jpg"},"buttons": '
        data_ex2 = ' [{"action": filter_check("네"),"label": "네","messageText": "네"},'
        data_ex3 = '{"action": self.send_response(0),"label": "이전으로","messageText": "이전으로"}]}}]}}'
        datatext = data_fr1 + data_fr2 + data_ex1 + data_ex2 + data_ex3
        responseBody = json.loads(datatext)

    if bot_resp == 5:
        allergy = db.search("알레르기 이름", a_filter, a_list)
        data_fr1 = '{"version": self.version,"template": {"outputs": [{"basicCard":'
        data_fr2 = '{"description": cur.answer_text(bot_resp, a_tags="%s")' % allergy
        data_ex1 = ',"thumbnail": {"imageUrl": "chatbot_image.jpg"},"buttons": '
        data_ex2 = ' [{"action": self.send_response(4),"label": "이전으로","messageText": "이전으로"},'
        data_ex3 = '{"action": self.send_response(0),"label": "처음으로","messageText": "처음으로"}]}}]}}'
        datatext = data_fr1 + data_fr2 + data_ex1 + data_ex2 + data_ex3
        responseBody = json.loads(datatext)

    else:
        data_fr1 = '{"version": self.version,"template": {"outputs": [{"basicCard":'
        data_fr2 = '{"description": cur.answer_text(7)'
        data_ex1 = ',"thumbnail": {"imageUrl": "chatbot_image.jpg"},"buttons": '
        data_ex2 = '[{"action": self.send_response(0),"label": "처음으로","messageText": "처음으로"}]}}]}}'
        datatext = data_fr1 + data_fr2 + data_ex1 + data_ex2
        responseBody = json.loads(datatext)

