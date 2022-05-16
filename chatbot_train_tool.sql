CREATE TABLE `chatbot_train_data` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `ner` VARCHAR(1024),
    `query` TEXT,
    `answer` TEXT NOT NULL,
    `answer_image` VARCHAR(2048)
)

INSERT INTO chatbot_train_data VALUES ('인사', , '안녕하세요', '반갑습니다.', );
INSERT INTO chatbot_train_data VALUES ('브랜드 입력', , '브랜드 이이름', '%s를 선택하였습니다. %s의 메뉴를 선택해 주십시오.', );
INSERT INTO chatbot_train_data VALUES ('메뉴 입력', , '메뉴이름', '%s를 선택하였습니다. %s이 가지고 있는 알러지는 다음과 같습니다.', );
INSERT INTO chatbot_train_data VALUES ('알러지 입력', , '알러지이름', '%s를 입력하였습니다. % 알러지 결과를 보여드립니다.', );
