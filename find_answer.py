class FindAnswer:
    def __init__(self, db):
        self.db = db

    def make_sql(self, intent):
        sql = "SELECT answer FROM 답변 "
        if intent != None:
            sql = sql + "WHERE intent_id = '{}'".format(intent)
        else:
            sql = sql + "WHERE intent_id = 6"
        return sql
    
    def search(self, q_tags, filter=False):
        franchise = self.db.exedata("SELECT 이름 FROM 프랜차이즈")
        menu = self.db.exedata("SELECT 메뉴이름 FROM 메뉴")
        allergy = self.db.exedata("SELECT 이름 FROM 유발물질")
        f_name = ""
        s_name = m_name = a_name = filter_list = []
        
        for tag in q_tags:
            #프랜차이즈명 입력
            if tag in franchise:
                if len(f_name) == 0 and not m_name and not a_name:
                    f_name = tag
                    m_name = a_name = []
                else:
                    f_name = ""
                    m_name = a_name = []
            #알레르기 성분 입력
            elif tag in allergy:
                if len(f_name) == 0 and not m_name:
                    filter_list.extend(tag)
                    self.filter_check()
                elif len(f_name) == 0 and len(m_name) == 1:
                    self.menu_find(m_name, filter_list=filter_list)
                else:
                    f_name = ""
                    m_name = a_name = []
            #메뉴명 입력
            elif tag not in franchise and tag not in allergy:
                if len(f_name) == 0 and not m_name and self.menu_find(tag):
                    f_name = ""
                    m_name = self.menu_find(tag, filter_list=filter_list)
                else:
                    f_name = ""
                    m_name = a_name = []
        return (f_name, m_name, a_name)

    def filter_check(self, check=''):
        if check == "네":
            return True
        else: return False

    def menu_find(self, tag, filter=False, filter_list=[]):
        m_name = []
        if not filter:
            m_name.extend(self.db.appdata("""
                SELECT 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴, 메뉴분류
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.메뉴이름 LIKE '%{}%'
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
                GROUP BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
                ORDER BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
            """.format(tag)))
        else:
            sql = """
                SELECT 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
                FROM 프랜차이즈, 메뉴, 메뉴분류
                WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                    AND 메뉴.메뉴이름 LIKE '%{}%'
                    AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                    AND 메뉴분류.프랜차이즈번호 = 프랜차이즈.고유번호
                    AND 메뉴.유발물질번호 = 유발물질.고유번호
                    AND 메뉴.분류번호 = 메뉴분류.분류번호
            """
            for fil in filter_list:
                sql = sql + " AND NOT(유발물질.이름 = '{}')".format(fil)
            sql = sql + """
                GROUP BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
                ORDER BY 프z랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름
            """
            m_name.extend(self.db.appdata(sql))
        return m_name

    def allergy_find(self, m_name):
        a_list = []

        a_list.append(self.db.exedata("""
            SELECT 유발물질.이름
            FROM 프랜차이즈, 메뉴, 메뉴분류, 유발물질
            WHERE 프랜차이즈.고유번호 = 메뉴.프랜차이즈번호
                AND 메뉴.프랜차이즈번호 = 메뉴분류.프랜차이즈번호
                AND 메뉴분류.프랜차이즈번호 = 프랜차이즈.고유번호
                AND 메뉴.유발물질번호 = 유발물질.고유번호
                AND 메뉴.분류번호 = 메뉴분류.분류번호
                AND 메뉴.메뉴이름 = '{}'
            GROUP BY 프랜차이즈.이름, 메뉴분류.분류이름, 메뉴.메뉴이름, 유발물질.이름
            ORDER BY 메뉴분류.분류이름, 메뉴.메뉴이름
        """.format(name)))
        return a_list

    def answer_text(self, intent_id, tags):
        intentsql = self.make_sql(intent_id)
        sql = self.db.exedata(intentsql)
        answer = ""
        if intent_id == 0:
            answer = sql.pop()
        elif intent_id == 1:
            answer = sql.pop()
        elif intent_id == 2:
            answer = sql.pop() % tags
        elif intent_id == 3:
            answer = sql.pop() % tags
        elif intent_id == 4:
            answer = sql.pop() % tags
        elif intent_id == 5:
            answer = sql.pop() % tags
        elif intent_id == 6:
            answer = sql.pop() % tags
        else:
            answer = sql.pop()
        return answer
