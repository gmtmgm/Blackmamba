CREATE TABLE 의도 (
    intent_id NUMBER NOT NULL,
    intent VARCHAR2(20),
    PRIMARY KEY(intent_id)
);

CREATE TABLE 메세지 (
    intent_id VARCHAR2(45) NOT NULL,
    question VARCHAR2 NOT NULL,
    answer VARCHAR2(170) NOT NULL,
    FOREIGN KEY(intent_id) REFERENCES 의도(intent_id)
);

INSERT INTO 의도(intent_id, intent) VALUES(1, '안내');
INSERT INTO 의도(intent_id, intent) VALUES(2, '프랜차이즈');
INSERT INTO 의도(intent_id, intent) VALUES(3, '메뉴');
INSERT INTO 의도(intent_id, intent) VALUES(4, '알레르기 성분 표시');
INSERT INTO 의도(intent_id, intent) VALUES(5, '알레르기 성분 입력');
INSERT INTO 의도(intent_id, intent) VALUES(6, '알레르기 성분 필터링');
INSERT INTO 의도(intent_id, intent) VALUES(7, '입력 실패');

INSERT INTO 메세지 (intent_id, question, answer) VALUES (1, '시작하기', '알레르기 보여줘, 챗봇 알보입니다!\n\n1. 아래의 버튼을 통해 프랜차이즈 목록을 확인할 수 있습니다.\n2. 메뉴 이름/프랜차이즈 명을 입력하여 검색할 수 있습니다.\n3. 알레르기 성분을 채팅으로 입력하여, 필터를 적용할 수 있습니다.');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (2, '프랜차이즈 목록','프랜차이즈 목록입니다.\n\n프랜차이즈 명을 선택하면 메뉴를 확인할 수 있습니다.');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (3, '도미노피자','%s 프랜차이즈에 등록된 메뉴 목록입니다. 메뉴를 선택하여 알레르기 성분을 확인할 수 있습니다.');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (3, '메뉴','%s 프랜차이즈에 등록된 메뉴 목록입니다. 메뉴를 선택하여 알레르기 성분을 확인할 수 있습니다.');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (4, '메뉴 입력','%s 프랜차이즈에 등록된 메뉴입니다.\n\n%s 메뉴 알레르기 성분\n\n%?.');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (5, '알레르기 성분 입력','%s에 포함된 성분입니다.\n%s가 포함된 매뉴를 필터링해서 보여줄까요?');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (6, '알레르기 성분 필터링 버튼','%s 성분이 포함된 메뉴를 필터링하였습니다. 이제부터 메뉴 검색시, %s 성분이 포함된 메뉴가 제외됩니다.');
INSERT INTO 메세지 (intent_id, question, answer) VALUES (7, 'DB에 존재하지 않는 이름', '등록되지 않은 프랜차이즈 또는 메뉴이거나, 이해할 수 없는 내용입니다.');
