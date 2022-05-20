import tensorflow as tf
from tag import *
from tensorflow import keras
import csv

q_sentences = [] #입력받은 질문 문장(우리 챗봇의 경우 리스트일 필요 없으니 추후 수정)
a_sentences = [] #답변 문장
sen_tag = [] #답변 태그
q_token = [] #질문 토크나이징

""" 입력 데이터 연동 과정 후 실행 """

for line in readdata:
    q_sentences.append(line['query'])
    a_sentences.append(line['answer'])
    if line[2] not in sen_tag:
        sen_tag.append(line['intent'])

for data in q_sentences:
    q_token.append(tokendatatokenize(data))

""" 품사 확인 후 메뉴 데이터베이스에서 비교 """
#나중에 데이터베이스 연결 파일 쪽으로 분리해야 할 듯

for token in q_token:
    if q_token[token][1] == 'FRL': #프랜차이즈 명을 알려달라는 입력을 받음
        """SELECT 이름
        FROM 프랜차이즈"""
    elif q_token[token][1] == 'FRC': #특정 프랜차이즈 명을 입력받음        
        """ """
    #메뉴 명을 알려달라는 입력을 받음
    #특정 메뉴 명을 입력받음
    #특정 알레르기 성분을 입력받음
    #특정 메뉴와 특정 알레르기 성분을 입력받음
    #특정 알레르기 성분을 2개 이상 입력받음
    
