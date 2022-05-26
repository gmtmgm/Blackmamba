class KakaoTemplate:
    def __init__(self):
        self.version = "2.0"


def simpleTextComponent(Self,text):
    return {
        "simpleText: {"text": text}
    }

def send_response(self,bot_resp):
    responseBody = {
        "version": self.version,
        "template":{
            "outputs": []
        }
    }

