CREATE TABLE �޴��з�(
�����������ȣ NUMBER NOT NULL,
�з���ȣ NUMBER NOT NULL,
�з��̸� VARCHAR2(20),
PRIMARY KEY(�����������ȣ,�з���ȣ),
FOREIGN KEY(�����������ȣ) REFERENCES ����������(������ȣ) ON DELETE CASCADE);

CREATE TABLE �޴�(
�����������ȣ NUMBER NOT NULL,
�з���ȣ NUMBER NOT NULL,
�޴�������ȣ NUMBER NOT NULL,
�޴��̸� VARCHAR2(20) NOT NULL,
���߹�����ȣ NUMBER,
PRIMARY KEY(�����������ȣ,�з���ȣ,�޴�������ȣ,���߹�����ȣ),
FOREIGN KEY(�����������ȣ,�з���ȣ) REFERENCES �޴��з�(�����������ȣ,�з���ȣ),
FOREIGN KEY(���߹�����ȣ) REFERENCES ���߹���(������ȣ));