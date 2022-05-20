from konlpy.tag import Komoran
import os

def datatokenize(data: str):
    #프랜차이즈 목록, 메뉴 이름, 알레르기 성분 입력 품사 태깅
    komoran = Komoran(userdic= './user_dic.txt')

    datatoken = komoran.pos(data)
    return datatoken

text = "프랜차이즈 목록을 살펴보고 있습니다."
text2 = "우유는 맛있습니다."
print(datatokenize(text))
