import requests, json
import cx_Oracle as cx
import intent_model
import find_answer

dsn = cx.makedsn("localhost", 1521, service_name= "XE")
db = cx.connect(user="c##Blackmamba", password="blackmamba", dsn=dsn)
cur = db.cursor()
a_filter = False
a_list = []

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

        if component == 0:
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": cur.answer_text(component),"buttonList": [ '
            data_ex1 = '{"type": "TEXT","data": {"title": "프랜차이즈 보기","code": self.send_message(1)}}]}]}}'
            datatext = data_fr1+data_fr2+data_ex1
            data = json.loads(datatext)

        if component == 1:
            f_list = []
            f_list.append(db.exedata('''SELECT 이름 FROM 프랜차이즈'''))
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": cur.answer_text(component, a_tags="프랜차이즈"),"buttonList": [ '
            datatext = data_fr1+data_fr2
            data_ex1 = []
            inte1, inte2 = 0
            for text1 in f_list:
                data_ex1[inte1] = '{"type": "TEXT","data": {"title": "%s","code": self.send_message(2,text1)}},' % text1
                inte1=inte1+1
            data_ex2 = ''' {"type": "TEXT","data": {"title": 뒤로가기","code": self.send_message(0)}}]}]}} '''
            for text2 in data_ex1:
                datatext = datatext+data_ex1[inte2]
                inte2 = inte2 + 1
            datatext = datatext+data_ex2
            data = json.loads(datatext)

        if component == 2:
            m_list = []
            m_list=db.menu_find("프랜차이즈 이름", a_filter, a_list)
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": cur.answer_text(component, a_tags="프랜차이즈 이름"),"buttonList": [ '
            datatext = data_fr1+data_fr2
            data_ex1 = []
            inte1, inte2 = 0
            for text1 in m_list:
                data_ex1[inte1] = '{"type": "TEXT","data": {"title": "%s","code": self.send_message(3,text1)}},' % text1
                inte1=inte1+1
            data_ex2 = ''' {"type": "TEXT","data": {"title": 뒤로가기","code": self.send_message(1)}}]}]}} '''
            for text2 in data_ex1:
                datatext=datatext+data_ex1[inte2]
                inte2 = inte2 + 1
            datatext=datatext+data_ex2
            data = json.loads(datatext)

        if component == 3:
            a_list_in_menu = []
            a_list_in_menu = db.allergy_find("메뉴 이름")
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": "%s" cur.answer_text(component, a_tags="메뉴 이름")' % "메뉴 이름"
            datatext = data_fr1+data_fr2
            inte1 = 0
            for text1 in a_list_in_menu:
                data_ex1[inte1] = '%s' % text1
                datatext = datatext + data_ex1
                inte1 = inte1 + 1
            data_ex1 = ' ,"buttonList": [ {"type": "TEXT","data": {"title": "이전으로","code": self.send_message(2)}}, '
            data_ex2 = ' {"type": "TEXT","data": {"title": "처음으로","code": self.send_message(0)}}]}]}} '
            datatext = datatext+data_ex1+data_ex2
            data = json.loads(datatext)

        if component == 4:
            allergy = db.search("알레르기 이름", a_filter, a_list)
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": cur.answer_text(component, a_tags="%s"),"buttonList": [ ' % allergy
            data_ex1 = ' {"type": "TEXT","data": {"title": "네","code": filter_check("네")}}, '
            data_ex2 = '{"type": "TEXT","data": {"title": "이전으로","code": self.send_message(0)}}]}]}} '
            datatext = data_fr1+data_fr2+data_ex1+data_ex2
            data = json.loads(datatext)

        if component == 5:
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": {"compositeList": '
            data_fr2 = '[{"description": cur.answer_text(component, a_tags="알레르기 이름"),"buttonList": [ '
            data_ex1 = '{"type": "TEXT","data": {"title": "이전으로","code": self.send_message(4)}},'
            data_ex2 = ''' {"type": "TEXT","data": {"title": 처음으로","code": self.send_message(0)}}]}]}} '''
            datatext = data_fr1+data_fr2+data_ex1+data_ex2
            data = json.loads(datatext)

        else:
            data_fr1 = ' {"event": "send","user": "al-2eGuGr5WQOnco1_V-FQ","compositeContent": "textContent": {'
            data_fr2 = '"text": cur.answer_text(7), "code": "self.send_message(0)", "inputType": "typing"}}]}]}}'
            datatext = data_fr1+data_fr2
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
