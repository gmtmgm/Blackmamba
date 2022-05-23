CREATE TABLE �ǵ� (
    intent_id NUMBER NOT NULL,
    intent VARCHAR2(20),
    PRIMARY KEY(intent_id)
);

CREATE TABLE �޼��� (
    intent_id VARCHAR2(45) NOT NULL,
    question VARCHAR2 NOT NULL,
    answer VARCHAR2(170) NOT NULL,
    FOREIGN KEY(intent_id) REFERENCES �ǵ�(intent_id)
);

INSERT INTO �ǵ�(intent_id, intent) VALUES(1, '�ȳ�');
INSERT INTO �ǵ�(intent_id, intent) VALUES(2, '����������');
INSERT INTO �ǵ�(intent_id, intent) VALUES(3, '�޴�');
INSERT INTO �ǵ�(intent_id, intent) VALUES(4, '�˷����� ���� ǥ��');
INSERT INTO �ǵ�(intent_id, intent) VALUES(5, '�˷����� ���� �Է�');
INSERT INTO �ǵ�(intent_id, intent) VALUES(6, '�˷����� ���� ���͸�');
INSERT INTO �ǵ�(intent_id, intent) VALUES(7, '�Է� ����');

INSERT INTO �޼��� (intent_id, question, answer) VALUES (1, '�����ϱ�', '�˷����� ������, ê�� �˺��Դϴ�!\n\n1. �Ʒ��� ��ư�� ���� ���������� ����� Ȯ���� �� �ֽ��ϴ�.\n2. �޴� �̸�/���������� ���� �Է��Ͽ� �˻��� �� �ֽ��ϴ�.\n3. �˷����� ������ ä������ �Է��Ͽ�, ���͸� ������ �� �ֽ��ϴ�.');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (2, '���������� ���','���������� ����Դϴ�.\n\n���������� ���� �����ϸ� �޴��� Ȯ���� �� �ֽ��ϴ�.');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (3, '���̳�����','%s ��������� ��ϵ� �޴� ����Դϴ�. �޴��� �����Ͽ� �˷����� ������ Ȯ���� �� �ֽ��ϴ�.');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (3, '�޴�','%s ��������� ��ϵ� �޴� ����Դϴ�. �޴��� �����Ͽ� �˷����� ������ Ȯ���� �� �ֽ��ϴ�.');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (4, '�޴� �Է�','%s ��������� ��ϵ� �޴��Դϴ�.\n\n%s �޴� �˷����� ����\n\n%?.');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (5, '�˷����� ���� �Է�','%s�� ���Ե� �����Դϴ�.\n%s�� ���Ե� �Ŵ��� ���͸��ؼ� �����ٱ��?');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (6, '�˷����� ���� ���͸� ��ư','%s ������ ���Ե� �޴��� ���͸��Ͽ����ϴ�. �������� �޴� �˻���, %s ������ ���Ե� �޴��� ���ܵ˴ϴ�.');
INSERT INTO �޼��� (intent_id, question, answer) VALUES (7, 'DB�� �������� �ʴ� �̸�', '��ϵ��� ���� ���������� �Ǵ� �޴��̰ų�, ������ �� ���� �����Դϴ�.');
