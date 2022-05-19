DELETE FROM 메세지;
CREATE TABLE IF NOT EXISTS 메세지 (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `intent` VARCHAR(45) NULL,
    `ner` VARCHAR(1024) NULL,
    `query` TEXT NULL,
    `answer` TEXT NOT NULL,
    PRIMARY KEY(`id`)
);
INSERT INTO 메세지 (intent, query, answer) VALUE ('시작', '안녕하세요', '알레르기 보여줘, 챗봇 알보입니다!\n\n1. 아래의 버튼을 통해 프랜차이즈 목록을 확인할 수 있습니다.\n2. 메뉴 이름/프랜차이즈 명을 입력하여 검색할 수 있습니다.\n3. 알레르기 성분을 채팅으로 입력하여, 필터를 적용할 수 있습니다.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('프랜차이즈 선택','프랜차이즈 보여주기 버튼','현재 입력된 프랜차이즈 목록입니다.\n\n프랜차이즈 명을 선택하면 메뉴를 확인할 수 있습니다.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('메뉴 선택', '프랜차이즈 버튼','%s 프랜차이즈에 등록된 메뉴 목록입니다. 메뉴를 선택하여 알레르기 성분을 확인할 수 있습니다.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('알레르기 성분 표시', '메뉴 버튼','%s 프랜차이즈에 등록된 메뉴 목록입니다. 메뉴를 선택하여 알레르기 성분을 확인할 수 있습니다.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('프랜차이즈 입력', '프랜차이즈 입력','%s 프랜차이즈에 등록된 메뉴 목록입니다. 메뉴를 선택하여 알레르기 성분을 확인할 수 있습니다.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('메뉴 입력', '메뉴 입력','%s 프랜차이즈에 등록된 메뉴입니다.\n\n%s 메뉴 알레르기 성분\n\n%?.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('알레르기 성분 입력', '알레르기 성분 입력','%s에 포함된 성분입니다.\n%s가 포함된 매뉴를 필터링해서 보여줄까요?');
INSERT INTO 메세지 (intent, query, answer) VALUE ('알레르기 성분 필터링','알레르기 성분 필터링 버튼','%s 성분이 포함된 메뉴를 필터링하였습니다. 이제부터 메뉴 검색시, %s 성분이 포함된 메뉴가 제외됩니다.');
INSERT INTO 메세지 (intent, query, answer) VALUE ('입력 실패','DB에 존재하지 않는 이름', '등록되지 않은 프랜차이즈 또는 메뉴이거나, 이해할 수 없는 내용입니다.');
