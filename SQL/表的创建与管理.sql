/*6.2.2�û��Զ�����������*/
--������������һ�����д洢��ͬ���͵����ݣ����û�����ȷ����Щ�о�����ͬ���������͡����Ⱥ�Ϊ����ʱ��
--����ʹ���û��Զ�����������
--��ʽ1��չ��jw1�ġ��ɱ��ԡ��������͡��ڵ㣬�һ��󣬡��½��������û��������͡�����ڴ򿪵ġ��½��û������������͡��е�
--�����桯�У����üܹ�ΪĬ��ֵdbo�����������룺StudentID;��������Ϊ��char;����Ϊ8��ȷ��
--��ʽ2��
/*USE jw1
CREATE TYPE dbo.StudentID1 FROM char(8) NOT NULL*/
/*6.3.1�������޸ĺ�ɾ����*/
--��ʽ1,������ϸ������ע�⣺���п�������ĳһ�ֶ��Զ���ţ�����������ʱ�����ظ�ֵ��ϵͳ�Զ������ֶ��ź�
/*USE jw1
CREATE TABLE Student
(StuNo StudentID NOT NULL,
ClassNo char(8) NOT NULL,
StuName char(20) NOT NULL)*/
/*6.3.2�޸ı�*/
--1.��ӱ��ֶΣ����ַ�ʽ����� ������
/*USE jw1
ALTER TABLE Student
ADD Birthday datetime NULL*/
--2.�޸ı��ֶ�
--���ַ�ʽ����ʾ2
/*USE jw1
ALTER TABLE Student
ALTER COLUMN StuName varchar(30) NOT NULL*/
--3.ɾ�����ֶ�
--���ַ�ʽ���ڶ���
/*USE jw1
ALTER TABLE dbo.Student
DROP COLUMN Birthday*/
/*6.3.3ɾ����*/
/*USE jw1
DROP TABLE dbo.Student*/
--������ɾ�������Ҫ������ṹ����ɾ���������ݣ�����ʹ��
--DELETE dbo.Student
--TRUNCATE TABLE dbo.Student
/*6.4 ��ӡ��޸ĺ�ɾ����������*/
--���⣬INSERT,UPDATE,DELETE
/*
�����������ĸ����裺ѡ������кͷ����߽�ֵ����������������ָ����η�������������������ָ�����������ķ������ļ���
�ϵ�λ�ã�����ʹ�÷��������ı��ָ��*/

