from konlpy.tag import Komoran

komoran = Komoran(userdic='./user_dic.tsv')
text = "프랜차이즈 목록을 살펴보고 있습니다."
text2 = "우유는 맛있습니다."
pos = komoran.pos(text)
print(pos)
pos = komoran.pos(text2)
print(pos)