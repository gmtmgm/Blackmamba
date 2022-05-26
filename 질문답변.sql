DROP TABLE 메세지;
DROP TABLE 답변;
DROP TABLE 의도;



CREATE TABLE 의도 (
    intent_id NUMBER NOT NULL,
    intent VARCHAR2(40),
    PRIMARY KEY(intent_id)
);

CREATE TABLE 답변 (
    intent_id NUMBER NOT NULL,
    answer_id NUMBER NOT NULL,
    answer VARCHAR2(500),
    PRIMARY KEY (answer_id, intent_id),
    FOREIGN KEY(intent_id) REFERENCES 의도(intent_id)
);

CREATE TABLE 메세지 (
    intent_id NUMBER NOT NULL,
    question VARCHAR2(200) NOT NULL,
    answer_id NUMBER NOT NULL,
    FOREIGN KEY(intent_id) REFERENCES 의도(intent_id)
    
);

INSERT INTO 의도(intent_id, intent) VALUES(0, '안내');
INSERT INTO 의도(intent_id, intent) VALUES(1, '프랜차이즈');
INSERT INTO 의도(intent_id, intent) VALUES(2, '메뉴');
INSERT INTO 의도(intent_id, intent) VALUES(3, '알레르기 성분 표시');
INSERT INTO 의도(intent_id, intent) VALUES(4, '알레르기 성분 입력');
INSERT INTO 의도(intent_id, intent) VALUES(5, '알레르기 성분 필터링');
INSERT INTO 의도(intent_id, intent) VALUES(6, '메뉴 알레르기성분 포함여부');
INSERT INTO 의도(intent_id, intent) VALUES(7, '오류');




INSERT INTO 답변(intent_id, answer_id, answer) VALUES (0, 0, '알레르기 보여줘, 챗봇 알보입니다!\n\n1. 아래의 버튼을 통해 프랜차이즈 목록을 확인할 수 있습니다.\n2. 메뉴 이름/프랜차이즈 명을 입력하여 검색할 수 있습니다.\n3. 알레르기 성분을 채팅으로 입력하여, 필터를 적용할 수 있습니다.\n4.메뉴 이름과 알레르기 성분을 입력하여, 포함 여부를 알 수 있습니다.');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (1, 1, '등록된 프랜차이즈 목록입니다.\n\n프랜차이즈 명을 선택하면 메뉴를 확인할 수 있습니다.');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (2, 2, '%s 프랜차이즈에 등록된 메뉴 목록입니다. 메뉴를 선택하여 알레르기 성분을 확인할 수 있습니다.');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (3, 3, '%s 프랜차이즈 - %s에 등록된 메뉴입니다.\n\n%s에 포함된 알레르기 성분: %s\n');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (4, 4, '%s에 포함된 성분입니다.\n%s(이)가 포함된 매뉴를 필터링해서 보여드릴까요?');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (5, 5, '%s 성분이 포함된 메뉴를 필터링하였습니다. 이제부터 메뉴 검색시, %s(이)가 포함된 메뉴가 제외됩니다.');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (6, 6, '%s 메뉴에 %s');
INSERT INTO 답변(intent_id, answer_id, answer) VALUES (7, 7, '등록되지 않은 프랜차이즈 또는 메뉴이거나, 이해할 수 없는 내용입니다.');

INSERT INTO 메세지(intent_id, question, answer_id) VALUES (0, '시작하기', 0);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (0, '시작', 0);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (0, '안녕?', 0);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (0, '처음으로', 0);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (0, '처음', 0);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈 목록',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈 명',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈 이름',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈명',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈 이름 보여줘',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '무슨 프랜차이즈 있어?',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (1, '프랜차이즈 목록 보여줄래?',1);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (2, 'BBQ',2);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (2, '공차 메뉴 보여줘',2);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (2, '홍루이젠 메뉴',2);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (2, '샐러디 메뉴 궁금해',2);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (2, '명랑 핫도그 메뉴',2);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (3, '소금우유도넛',3);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (3, '카페라떼',3);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (4, '성분 우유',4);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (4, '성분 메밀',4);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (4, '성분 밀',4);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (4, '돼지고기',4);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (5, '알레르기 성분 필터링 버튼',5);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (6, '황금올리브치킨 돼지고기',6);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (6, '양념맵소킹 우유',6);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (6, '페퍼로니 쇠고기',6);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (6, '베이컨 토마토 디럭스 토마토',6);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '아무 말이나 해보자', 7);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '오늘 날씨 어때?', 7);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '아무 말이나 해보자', 7);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '메뉴 추천 해줘', 7);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '만들기 힘들어요', 7);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '굳이 오류 관련 의도를 지정할 필요가 있었나?', 7);
INSERT INTO 메세지(intent_id, question, answer_id) VALUES (7, '필요 없으면 걍 빼야지', 7);

commit;
