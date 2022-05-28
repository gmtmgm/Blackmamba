from tokenizing import Preprocess

class FindAnswer:
    def __init__(self, db):
        self.db = db

    def make_sql(self, intent):
        sql = "SELECT answer FROM 답변 "
        if intent != None:
            sql = sql + "WHERE intent_id = '{}'".format(intent)
        else:
            sql = sql + "WHERE intent_id = 7"
        return sql
    
    def query_check(self, query):
        if query == "이전으로" or query == "처음으로":
            return 0

    def sort_tags(self, keywords):
        franchise = self.db.exedata("SELECT 이름 FROM 프랜차이즈")
        menu = self.db.exedata("SELECT 메뉴이름 FROM 메뉴")
        allergy = self.db.exedata("SELECT 이름 FROM 유발물질")
        one = ["프랜차이즈", "프랜차이즈 목록", "프랜차이즈명"]
        
        f_tags = []
        m_tags = []
        a_tags = []
        if len(list(keywords)) > 1:
            for tag in keywords:
                if tag in one:
                    return(1, '')
                elif tag in franchise:
                    f_tags.append(tag)
                elif tag in allergy:
                    a_tags.append(tag)
                elif self.menu_find(tag):
                    m_tags.append(tag)
                
        else:
            keyword = "".join(keywords)
            if keyword in one:
                return(1, '')
            elif keyword in franchise:
                f_tags.append(keyword)
            elif keyword in allergy:
                a_tags.append(keyword)
            elif self.menu_find(keyword):
                m_tags.append(keyword)
            
        f_len = len(f_tags)
        m_len = len(m_tags)
        a_len = len(a_tags)
        print(f_len, m_len, a_len)
        print(f_tags, m_tags, a_tags)
        if f_len == 1 and m_len == 0 and a_len == 0: #프랜차이즈 이름 입력받음
            return (2, f_tags)
        elif f_len == 0 and m_len == 1 and a_len == 0: #메뉴 이름 입력받음
            return (3, m_tags)
        elif f_len == 0 and m_len == 0 and a_len >= 1: #알레르기 성분 입력받음
            return (4, a_tags)
        elif f_len == 0 and m_len == 1 and a_len >= 1: #메뉴와 알레르기 성분
            return (6, m_tags, a_tags)
        else:
            return (7, '')

    def search(self, tags, filter=False):
        intent_id = tags[0]
        print(tags[1])
        if intent_id == 1:
            return ""
        elif intent_id == 2:
            return self.small_menu_find(tags[1]) #소분류 목록 반환
        elif intent_id == 3:
            return self.f_menu_find(tags[1]) #메뉴 목록 반환
        elif intent_id == 4:
            return tags[1] #알레르기 리스트 반환
        elif intent_id == 6:
            return self.allergy_check(tags[1], tags[2]) #문장 반환
        else:
            return 
        
    def filter_check(self, check=''):
        if check == "네":
            return True
        else: return False
    
    def fran_find(self): #프랜차이즈 목록 리턴
        f_list = []
        f_list.extend(self.db.exedata("""
            SELECT 프랜차이즈.이름
            FROM 프랜차이즈
            ORDER BY 프랜차이즈.이름
        """))
        return f_list
    
    def small_menu_find(self, f_tag): #소분류 목록 리턴
        sm_list = []
        f_tag = "".join(f_tag)
        sm_list.extend(self.db.exedata("""
            SELECT 프랜차이즈.이름 || ' - ' || 메뉴분류.분류이름
            FROM 프랜차이즈, 메뉴분류
            WHERE 프랜차이즈.고유번호 = 메뉴분류.프랜차이즈번호
                AND 프랜차이즈.이름 = '{}'
            GROUP BY 프랜차이즈.이름, 메뉴분류.분류이름
            ORDER BY 프랜차이즈.이름, 메뉴분류.분류이름
        """.format(f_tag)))
        return sm_list
    
    #프랜차이즈명과 소분류로 메뉴 추출
    def small_to_menu(self, f_tag, sm_tag, filter=False, filter_list=[]): 
        m_list = []
        if not filter:
            m_list.extend(self.db.exedata("""
                SELECT 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴, 메뉴분류
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                    AND 프랜차이즈.이름 = '{}'
                    AND 메뉴분류.분류이름 = '{}'
                GROUP BY 메뉴.메뉴이름
                ORDER BY 메뉴.메뉴이름
            """.format(f_tag, sm_tag)))
        else:
            sql = """
                SELECT 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴, 메뉴분류, 유발물질
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴분류.프랜차이즈번호 = 프랜차이즈.고유번호
                    AND 메뉴.유발물질번호 = 유발물질.고유번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                    AND 프랜차이즈.이름 = '{}'
                    AND 메뉴분류.분류이름 = '{}'
                    AND NOT 메뉴.메뉴이름 IN (SELECT 메뉴.메뉴이름
                        FROM 프랜차이즈, 메뉴, 유발물질
                        WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
            """.format(f_tag, sm_tag)
            if len(filter_list) > 1:
                for filt in filter_list:
                    sql = sql + " AND 유발물질.이름 = '{}'".format(filt)
                sql = sql + """
                    AND 메뉴.유발물질번호 = 유발물질.고유번호)
                    GROUP BY 메뉴.메뉴이름
                    ORDER BY 메뉴.메뉴이름
                """
            else:
                sql = sql + """ AND 유발물질.이름 = '{}'
                AND 메뉴.유발물질번호 = 유발물질.고유번호)
                    GROUP BY 메뉴.메뉴이름
                    ORDER BY 메뉴.메뉴이름""".format(filter_list)
            m_list.extend(self.db.exedata(sql))
        return m_list
    
    #메뉴이름만 목록 리턴
    def menu_find(self, m_tag, filter=False, filter_list=[]): 
        m_list = []
        if not filter:
            m_list.extend(self.db.exedata("""
                SELECT 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴분류, 메뉴
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.메뉴이름 LIKE '%{}%'
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                GROUP BY 메뉴.메뉴이름
                ORDER BY 메뉴.메뉴이름
            """.format(m_tag)))
        else:
            sql = """
                SELECT 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴, 메뉴분류, 유발물질
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.메뉴이름 LIKE '%{}%'
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴분류.프랜차이즈번호 = 프랜차이즈.고유번호
                    AND 메뉴.유발물질번호 = 유발물질.고유번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                    AND NOT 메뉴.메뉴이름 IN (SELECT 메뉴.메뉴이름
                        FROM 프랜차이즈, 메뉴, 유발물질
                        WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
            """
            if len(filter_list) > 1:
                for filt in filter_list:
                    sql = sql + " AND 유발물질.이름 = '{}'".format(filt)
                sql = sql + """
                    AND 메뉴.유발물질번호 = 유발물질.고유번호)
                    GROUP BY 메뉴.메뉴이름
                    ORDER BY 메뉴.메뉴이름
                """
            else:
                sql = sql + """ AND 유발물질.이름 = '{}'
                    AND 메뉴.유발물질번호 = 유발물질.고유번호)
                    GROUP BY 메뉴.메뉴이름
                    ORDER BY 메뉴.메뉴이름""".format(filter_list)

            m_list.extend(self.db.exedata(sql))
        return m_list

    #프랜차이즈,소분류,메뉴를 하나의 텍스트로 리턴
    def f_menu_find(self, m_tag, filter=False, filter_list=[]): 
        m_list = []
        if not filter:
            m_list.extend(self.db.exedata("""
                SELECT 프랜차이즈.이름 || ' 프랜차이즈 - ' || 메뉴분류.분류이름
                || ' 분류의 ' || 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴분류, 메뉴
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.메뉴이름 LIKE '%{}%'
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                GROUP BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
                ORDER BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
            """.format(m_tag)))
        else:
            sql = """
                SELECT 프랜차이즈.이름 || ' 프랜차이즈 - ' || 메뉴분류.분류이름
                || ' 분류의 ' || 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴, 메뉴분류, 유발물질
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.메뉴이름 LIKE '%{}%'
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴분류.프랜차이즈번호 = 프랜차이즈.고유번호
                    AND 메뉴.유발물질번호 = 유발물질.고유번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                    AND NOT 메뉴.메뉴이름 IN (SELECT 메뉴.메뉴이름
                        FROM 프랜차이즈, 메뉴, 유발물질
                        WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
            """
            if len(filter_list) > 2:
                for filt in filter_list:
                    sql = sql + " AND 유발물질.이름 = '{}'".format(filt)
            else:
                sql = sql + " AND 유발물질.이름 = '{}'".format(filter_list)
            sql = sql + """
                AND 메뉴.유발물질번호 = 유발물질.고유번호)
                GROUP BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
                ORDER BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
            """
            m_list.extend(self.db.exedata(sql))
        return m_list

    def allergy_find(self, m_tag): #알레르기 성분 목록 리턴
        a_list = []
        a_list.extend(self.db.exedata("""
            SELECT 유발물질.이름
            FROM 프랜차이즈, 메뉴, 메뉴분류, 유발물질
            WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                AND 메뉴분류.프랜차이즈번호 = 프랜차이즈.고유번호
                AND 메뉴.유발물질번호 = 유발물질.고유번호
                AND 메뉴.분류번호 = 메뉴분류.분류번호
                AND 메뉴.메뉴이름 = '{}'
            GROUP BY 유발물질.이름
            ORDER BY 유발물질.이름
        """.format(m_tag)))
        return a_list
    
    def allergy_check(self, m_tag, a_list): #메뉴에 성분이 포함되어 있는지
        a_include = ""
        a_exclude = ""
        for a in a_list:
            if a in self.allergy_find(m_tag):
                a_include = a_include + "%s | " % a
            else:
                a_exclude = a_exclude + "%s | " % a
        if a_include and a_exclude:
            return a_include + "(이)가 포함되어 있고" + a_exclude + "(이)가 포함되어 있지 않습니다."
        elif a_include and not a_exclude:
            return a_include + "(이)가 포함되어 있습니다."
        else:
            return a_exclude + "(이)가 포함되어 있지 않습니다."


    def answer_text(self, keywords):

        tags = self.sort_tags(keywords)
        intent_id = tags[0]
        intentsql = []
        tag = []
        intentsql.extend(self.db.exedata(self.make_sql(intent_id)))
        answer = self.search(tags)
        if intent_id == 1:
            return(intentsql.pop())
        elif intent_id == 2:
            tag.extend(tags)
            return(intentsql.pop() % tags[1].pop())
        elif intent_id == 3:
            print("다음과 같은 메뉴가 등록되어 있습니다.")
        elif intent_id == 4:
            s = ""
            for a in answer:
                print(a)
                s = s + ("%s | " % a)
                print(s)
            return(s + intentsql.pop())
        elif intent_id == 6:
            return(intentsql.pop() % tag[1] + answer)
        print(answer)
        return answer



