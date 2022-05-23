from konlpy.tag import Komoran
import os

class Preprocess:
    def __init__(self, userdic= './user_dic.txt'):
        self.komoran = Komoran(userdic=userdic)
        #NNP 태그 제외하고 모두 사용하지 않음
        self.include_tags = ['NNP']

    def pos(self, sentence):
        return self.komoran.pos(sentence)
    
    def get_keywords(self, pos, with_tag=True):
        f = lambda x: x in self.include_tags
        word_list = []
        for p in pos:
            if f(p[1]) is True:
                word_list.append(p if with_tag is True else p[0])
        return word_list
