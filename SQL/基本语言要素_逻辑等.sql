/*
USE jw
--����ע��
/*�����Ƕ���ע��*/
SELECT * FROM dbo.Class --��ѯ�������
*/

--�����ֲ�����

/*
DECLARE
{@local_variable [AS] data_type
| @cursor_variable_name CURSOR
}-- [ , ...n]
@local_variable ����ָ���ֲ����������ƣ�����data_type�û����þֲ��������������͡�
�ڶ������α����������@cursor_variable_name���α��������[ , ...n]��ʾһ��declare�����������������
����֮��Ӧ�ö��Ÿ���
DECLARE @a char(10),@b varchar(10) 
SELECT @a=2,@b=3
--SET @a=2 ,SET���ֻ�ܶԵ���������ֵ��SELECT��ͬʱ�Զ��������ͨ��SELECT����ѯ�����ֵ��ĳ������
*/

--�ڱ�ʾ����ʹ��

/*
DECLARE @Score decimal--����һ�������͵ľֲ�����Score
SELECT @Score=85.0--��ֵ
USE jw
SELECT * FROM dbo.Score WHERE Score=@Score--��ѯ
*/

--ȫ�ֱ��������Ա��κ��κγ���ʹ�ã�ͨ���洢�����趨ֵ��ͳ�����ݣ�����������ϵͳ���趨ֵ��ִ��T-SQL������״ֵ̬

/*
--ʹ��@@
--ʹ��ȫ�ֱ���@@VERSION���鿴��ǰʹ�õ�sql�汾��Ϣ
SELECT @@VERSION
*/

--�����

--��ִ֮���������㣬�ַ����������������ֵ�������λ��������Ƚ���������߼������
/*
--1.�����������+��-��*,/,%(ȡģ)
--ע�⣺���������������ʽ������������ô���ֻ��ȡ������С��ֵ��ȥ��ȡģ���㣬������������������
SELECT 2.5+3.5
SELECT 2.5-3.5
SELECT 2.5*3.5'�����ͳ�'
SELECT 2.5/3.5'�����ͳ�'
SELECT 2/3'������'
SELECT 2%3
*/
--2.��ֵ�������=�������Ǹ�ֵ���ѯ��WHERE��
/*
--1)��ֵ
DECLARE @name varchar(20)
SET @name='��÷��'
--2)��ѯ
USE jw
SELECT * FROM dbo.Student WHERE StuName=@name
*/
--3λ������������ڶ��������ݼ�ִ��λ������&�룬|��^��򣬵���һ��Ϊ��ʱΪ1
/*
SELECT 1&0
SELECT 1&1
SELECT 1|0
SELECT 1^0
*/
--4.�Ƚ�������������������ʽ�Ƿ���ͬ=��>,<,>=,<=,!=(<>),!<(��С��)��!>
/*
USE jw
SELECT * FROM dbo.Score WHERE Score>=70.0
*/
--5.�߼������������TRUE��FALSE��AND,OR,NOT,BETBEWWN,EXISTS,IN,LIKE,ALL,ANY,SOME
--EXISTS������Ӳ�ѯ����������ĳ��Ԫ�أ�����true
--IN��������������������е�ĳ��Ԫ��
--LIKE�������������һ��ģʽ��ƥ��
--ALL��������еĶ�Ϊtrue
/*
USE jw--��ѯѧ������������λ�ó���%��%���������ѧ����Ϣ
SELECT * FROM dbo.Student WHERE StuName LIKE '%��%' OR StuName LIKE '��%'--��*����ClassNo��
*/
--6.�ַ��������������+
/*
USE jw
SELECT 'ѧ�ţ�'+StuNo+'�༶��'+ClassNo+'������'+StuName FROM dbo.Student--ʹ��ʾ����������Ķ�
*/

--���������������ú���Ҳ���Զ��庯�������潫���ú���������

--�м����������ؿ���sql������������һ��ʹ�õĶ���
--�ۺϺ�������һ��ֵ�������㣬������һ������ֵ
--�����������Է����е�ÿһ�о�����һ������ֵ
--�����������Ե�һֵ�������㣬Ȼ�󷵻ص�һֵ��ֻҪ���ʽ��Ч������ʹ�ñ�������
   --����������Ϊ���ú������α꺯�������ں�ʱ�亯���ȡ�
--1.���ں�����GETDATE()���ص�ǰ���ڣ���YEAR,MONTH,DAY,�ֱ𷵻�ָ�����ڵ�������
/*
SELECT 
GETDATE() AS ��ǰ����,
YEAR(GETDATE()) AS ��,
MONTH(GETDATE()) AS ��,
DAY(GETDATE()) AS ��
*/
--2.�ۺϺ�����AVG,MIN,MAX,SUM
--ƽ��ֵ
/*
USE jw
SELECT AVG(Score) AS 'ƽ����' FROM Score 
SELECT MIN(Score) AS '��Сֵ' FROM dbo.Score
*/
--3.����������ROW_NUMBER()ͳ������
/*
USE jw
SELECT StuNo,CouNo,Score,ROW_NUMBER() OVER (ORDER BY Score DESC) AS '����' FROM dbo.Score--�¼���һ������
*/
--4.����������ʹ�ã�ͨ��LTRIM()ɾ���ַ��������е���ʼ�ո�
/*
DECLARE @string_to_ltrim varchar(30)
SET @string_to_ltrim='    HELLO WORLD'
SELECT @string_to_ltrim AS 'ԭʼ�ַ�'
SELECT LTRIM(@string_to_ltrim) AS 'ȥ����ʼ�ո�'
*/

--���̿������ IF-ELSE,CASE,WHILE, GOTO,WAITFOR

--1.IF-ELSE ���
/*
DECLARE @a int,@b int,@c int
SELECT @a=2,@b=3,@c=4
IF @a>@b
PRINT 'X>Y'
ELSE IF @b>@c
PRINT'Y>Z'
ELSE PRINT 'Z>Y'
*/
--2.begin with.while,case,if ...else,�����ж�����䣬����Ҫ��begin end�����������
--3.GO���.GO��䲻��T-SQL���,���߲�����ͬһ��
/*
USE jw
GO
DECLARE @MyMsg Varchar(50)
SELECT @MyMsg='HELLO WORLD'
GO
*/
--4.CASE ��䡣�ɼ������������ʽ���������з��������Ľ�����ʽ���ء���Ϊ��CASE��������CASE���
--1����case
/*
--��������
CASE sex
WHEN '1' THEN '��'
WHEN '0' THEN 'Ů'
ELSE '����'
end
CASE --����
WHEN sex='1' THEN '��'
WHEN sex='0' THEN 'Ů'
ELSE '����'
end

USE jw
SELECT StuNo,CouNo,level=
CASE
WHEN Score>=90 THEN 'A'
WHEN Score<90 AND Score>=75 THEN 'B'
WHEN Score<75 and Score>=60 THEN 'C'
ELSE 'D'
END
FROM dbo.Score
*/
--5.WHILE..CONTINUE..BREAK���
/*
DECLARE @INDEX INT=0,@ENDINDEX INT =0
WHILE @INDEX<5
	BEGIN
		SET @ENDINDEX=@ENDINDEX+1
		PRINT @ENDINDEX
		WHILE @ENDINDEX>5
			BEGIN 
				PRINT '��ֹ��ѭ��'
				BREAK--һ������ѭ������break����ô������ѭ��,�����Ҳ��ѭ��,�������ѭ��
			END
		CONTINUE--��IF��䲻����ʱ��������һ�׶�
		SET @INDEX=@INDEX+1
	END
*/
--6.GOTO���.��ִ�������������ת����ǩ�������ӱ�ǩ��λ�ü�������
/*8
DECLARE @x int
SELECT @x=0
label_1:
	SELECT @x=@x+1
	PRINT @x
	WHILE @x<6
GOTO label_1
*/
--7.WITHFOR ��䣬�ӳ���䣬�����趨�ڵ���ָ��ʱ���ʱ����֮ǰ�����ֱ�ʾ��ʽ
/*
USE jw
WAITFOR DELAY '01��02��03'--�ȴ�1Сʱ2��3���ִ��SELECT���
SELECT * FROM Student
--��
WAITFOR TIME '23��08��00'--�ȵ�1Сʱ8�ֺ��ִ��
SELECT * FROM Student
*/
--8.RETURN ��䣻
--RETURN ����û��Ӳ�ѯ��������������˳�����֮�������ǲ�ִ�еģ����ڴ洢����ʱ��RETURN�ǲ��ܷ��ؿ��Ƶġ�
--����ͼ���ؿ�ֵ�������ɾ�����Ϣ������0 
/*
USE jw
GO
CREATE PROCEDURE checkscore
AS
IF(SELECT Score FROM dbo.Score WHERE StuNo=0463501101 AND CouNo=001)>60
	RETURN 1
ELSE 
	RETURN 0
*/


