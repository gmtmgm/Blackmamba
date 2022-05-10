CREATE TABLE 메뉴분류(
프랜차이즈번호 NUMBER NOT NULL,
분류번호 NUMBER NOT NULL,
분류이름 VARCHAR2(20),
PRIMARY KEY(프랜차이즈번호,분류번호),
FOREIGN KEY(프랜차이즈번호) REFERENCES 프랜차이즈(고유번호) ON DELETE CASCADE);

CREATE TABLE 메뉴(
프랜차이즈번호 NUMBER NOT NULL,
분류번호 NUMBER NOT NULL,
메뉴고유번호 NUMBER NOT NULL,
메뉴이름 VARCHAR2(20) NOT NULL,
유발물질번호 NUMBER,
PRIMARY KEY(프랜차이즈번호,분류번호,메뉴고유번호,유발물질번호),
FOREIGN KEY(프랜차이즈번호,분류번호) REFERENCES 메뉴분류(프랜차이즈번호,분류번호),
FOREIGN KEY(유발물질번호) REFERENCES 유발물질(고유번호));