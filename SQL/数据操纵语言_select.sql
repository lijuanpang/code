--1.SELECT���
/*
SELECT [ALL|DISTINCT] select_list
	[INTO new_table]
	FROM table_list
	[WHERE search_conditions]
	[GROUP BY group_by_list]
	[HAVING search_conditions]
	[ORDER BY order_list[ASC|DESC]]
	*/
--1.1������ѯ
USE jw
--SELECT * FROM dbo.Class--��ȡ�������е���Ϣ�������ձ��е�˳�����ʽ��������
--SELECT ClassNo,ClassName FROM dbo.Class--��ȡ����ָ����һ�л�������
--SELECT ClassNo AS CN1,ClassName AS CN2 FROM dbo.Class--�ڷ��ؽ���ж��������������ı���е�����
--SELECT DISTINCT ClassNo,ClassName FROM dbo.Class--��DISTINCT �ؼ���ɾ���ظ���
--SELECT TOP 5 ClassNo,ClassName FROM dbo.Class--���ز�ѯ������������Ǳ����������µ�n����Ϣ
--1.2 ������ѯwhere
--SELECT * FROM dbo.Class WHERE ClassNo='20040001'--ʹ�������
--SELECT * FROM dbo.Score WHERE Score>60 AND Score<80--ʹ���߼������AND or
--SELECT * FROM dbo.Score WHERE NOT Score>60--ʹ��NOT
/*IN������ȡֵ�Ƿ�����ĳһȡֵ���ϣ�IN ��NOT IN*/
--SELECT * FROM dbo.Class WHERE DepartNo IN ('01','02')--IN������ѯ�б��и�ֵ�����������ͬ����������
--SELECT * FROM dbo.Score WHERE Score BETWEEN '60' AND '80' /*BETWEEN ������ĳһ��Χ��NOT BETWEEN*/
/*ģ����ѯ��like��ͨ��� %���������ַ�._:�����ַ�.[] ��ָ����Χ�ڵĵ����ַ�.[^]������ָ����Χ�ڵĵ����ַ�*/
--SELECT CouNo FROM dbo.Course WHERE Teacher LIKE '��%'--���ŵ���ʦ%
--SELECT CouNo FROM dbo.Course WHERE DeparNo like '0_',--ʹ����Ч_
--SELECT * FROM dbo.Course WHERE CouNo like '[01]%'--��0��1��ͷ�����пγ���Ϣ
/*IS NOT NULL����*/
--SELECT * FROM dbo.Course WHERE CouNo IS NOT NULL
--1.3.�ۺ������GROUP BY,HAVING��
/*GROUP BY,���Զ�ĳһ�����ݵ�ֵ���з���*/--GROUP BY [ALL] <column>[,<column_name>...]ALL��ʾ�Ƿ�ʹ��������Ϣ������where����
--ͨ����ۺϺ�������ʹ�ã�SUM,AVG,MAX,MIN,COUNT(��������������������)
--SELECT CouNo,AVG(Score) AS 'ƽ���ɼ�' FROM dbo.Score GROUP BY CouNo  
--SELECT AVG(Score) AS 'ƽ���ɼ�' FROM dbo.Score WHERE CouNo='001'--�����������ܵ�ƽ����������SELECT���һ�� CouNo���ʹ���
--SELECT CouNo,AVG(Score) AS 'ƽ���ɼ�' FROM dbo.Score WHERE CouNo='001' GROUP BY CouNo--��ʱ��ҪGROUP BY 
/*HAVING�Ӿ䣬��GROUP BY��ͬʹ�á�WHERE�����޶�ÿһ�еĲ�ѯ��������HAVING�����޶�����ͳ��ֵ*/
--SELECT *FROM table WHERE search_condition1 GROUP BY column_name HAVING search_condition2
--SELECT CouNo,AVG(Score) AS 'ƽ���ɼ�' FROM dbo.Score WHERE CouNo LIKE '[01]%'  
--GROUP BY CouNo HAVING AVG(Score)>80
/*��������콣��Ҫ�ڷ���֮ǰ��Ӧ�ã�����WHERE;��HAVING������GROUP BY֮�������ڽ��������֮���ڽ����ж�
���⣬�ۺϺ���������SELECT��HAVING��ʹ�ã���������where��ʹ��*/
/*ORDER BY */--һ���û�SELECT�����󣬶Բ�ѯ���ص����ݽ����������������
--ORDER BY order_expression[ASC|DESC]
/*order_expression���������еı����ͱ��ʽ�����ж��������ʱ���ö��Ÿ����������Ը�����Ҫ��Ĭ��Ϊ����ASC*/
--SELECT CouNo,AVG(Score) AS 'ƽ���ɼ�' FROM dbo.Score GROUP BY CouNo HAVING AVG(Score)>80 ORDER BY AVG(Score) DESC
--1.4����ѯ ���Ƚ�����֮�������
--��������-�ѿ����˻� �������ÿһ����ˣ�ûʲô��
--SELECT * FROM dbo.Score,dbo.Course
/*������Ҫ��WHERE����������һ��N������N-1����������*/
--SELECT ClassNo,DepartName FROM dbo.Class,dbo.Department WHERE dbo.Class.DepartNo=dbo.Department.DepartNo
/*---������������
---SELECT���������ڼ������ж����ڣ���ôҪע���������ƣ�FROM��������ʹ�õ��Ļ������ƣ�WHERE����һ��ͬ������*/
--��ѯѧ��Ϊ0463501101��ͬѧ�����֣��༶��ţ����Ƽ�ϵ���������
/*
SELECT StuNo,StuName,dbo.Student.ClassNo,ClassName,dbo.Class.DepartNo,DepartName 
FROM dbo.Student,dbo.Class,dbo.Department
WHERE dbo.Student.ClassNo=dbo.Class.ClassNo AND dbo.Class.DepartNo=dbo.Department.DepartNo AND dbo.Student.StuNo='0463501101'
*/
---��һ�������﷨��ʽ��ʹ��ANSI����INNER JOIN�������Ӳ�ѯ����������INNER����ʡ�ԣ���ON�Ӿ��и�����������
--SELECT select_list FROM table1 INNER JOIN table2[ON jion_condition] [WHERE search_conditions]
--��ѯѧ��Ϊ0463501101��ͬѧ�����֣��༶��ţ�����
--USE jw
--SELECT StuName,dbo.Student.ClassNo,ClassName FROM dbo.Student INNER JOIN dbo.Class ON dbo.Student.ClassNo=dbo.Class.ClassNo WHERE dbo.Student.StuNo=0463501101
/*�����ӷ�Ϊ��ֵ���ӣ���Ȼ���Ӻͷǵ�ֵ����*/
/*��ֵ���ӣ�ʹ��=,������г������ӱ��е������У������ظ���*/
USE jw--ѧ����Ϣ���༶��Ϣ
--SELECT * FROM dbo.Student,dbo.Class WHERE dbo.Student.ClassNo= dbo.Class.ClassNo--�������ClassNo���ظ���
--ʹ��ANSIʱ
--SELECT * FROM dbo.Student INNER JOIN dbo.Class ON dbo.Student.ClassNo= dbo.Class.ClassNo--���������ͬ
/*��Ȼ���ӣ�ʹ��=����ɾ���ظ���*/                 --����һһ�г�
--SELECT StuNo,dbo.Student.ClassNo,StuName,DepartNo,ClassName FROM dbo.Student,dbo.Class WHERE dbo.Student.ClassNo= dbo.Class.ClassNo
/*�ǵ�ֵ���ӣ�����=��<>��*/    
--SELECT dbo.Student.StuNo,StuName,CouNo,Score FROM dbo.Student,dbo.Score WHERE dbo.Student.StuNo=dbo.Score.StuNo AND Score>90
--SELECT dbo.Student.StuNo,StuName,CouNo,Score FROM dbo.Student INNER JOIN dbo.Score ON dbo.Student.StuNo=dbo.Score.StuNo WHERE Score>90
/*������*/
/*�����ӣ�������Ϣ��ʧ�������ӱ�֮�֣�������ÿ�е�����ȥƥ��ӱ��е������У���û���ҵ�ƥ���У����������Ȼ���������ؽ������Ӧ�Ĵӱ��б�����NULL����*/
/*��Ϊ�������ӣ��������ӣ�ȫ������*/
--�������ӣ� JOIN����������ұ�Ϊ�ӱ�
--SELECT select_list FROM table1 LEFT OUTER JOIN table2[ON jion_condition] [WHERE search_conditions]
--SELECT dbo.Course.CouNo,CouName,StuNo,Score FROM dbo.Course LEFT OUTER JOIN dbo.Score ON Course.CouNo=Score.CouNo AND Score>90
/*�������ӣ� JOIN�ұ����������Ϊ�ӱ�*/ --RIGHT OUTER JOIN
--SELECT CouNo,CouName,dbo.Department.DepartNo,DepartName FROM dbo.Course RIGHT OUTER JOIN dbo.Department ON dbo.Course.DeparNo=dbo.Department.DepartNo
/*ȫ�����ӣ�������*/ --FULL OUTER JOIN
--SELECT dbo.Student.StuNo,StuName,CouNo,Score FROM dbo.Student FULL OUTER JOIN dbo.Score ON dbo.Student.StuNo=dbo.Score.StuNo
/*ע�⣺on��where����1�� on��������������ʱ��ʱʹ�õ�������������on�е������Ƿ�Ϊ�棬���᷵����߱��еļ�¼��*/
--2��where����������ʱ�����ɺú��ٶ���ʱ����й��˵���������ʱ�Ѿ�û��left join�ĺ��壨���뷵����߱�ļ�¼���ˣ�������Ϊ��ľ�ȫ�����˵���
/*��������*/
/*����������Ӳ���where�Ӿ䣬�򷵻صĽ���Ǳ����ӵ�������ĵѿ����˻��������������������ĵѿ����˻���ȥwhere���޶���ʡ�Ե�����*/
--SELECT select_list FROM table CROSS JOIN table [WHERE search_conditions]
USE jw
--SELECT * FROM dbo.Class CROSS JOIN dbo.Department--�ͣ���Ч��һ��
/*������*/
--�Լ������Լ���ѯ�������ǿγ���ͬ����ʦ��ͬ�Ŀγ���Ϣ��
--SELECT t1.CouNo,t1.CouName,t1.Teacher FROM Course t1,Course t2 WHERE t1.CouName=t2.CouName AND t1.Teacher !=t2.Teacher
--���ϲ�ѯʱ��Course��������������t1��t2�����ڶ�������IAO�������Ӳ�ѯ
/*��������*/
--����ͬ�Ĳ�ѯ��������������ӣ�
/*
SELECT select_list FROM table_source [WHERE search_condition]
{UNION[ALL]
SELECT select_list FROM table_source [WHERE search_condition] }  [ORDER BY order_expression]
UNION �ڲ��� SELECT ������ӵ����ͬ�������С���Ҳ����ӵ�����Ƶ��������͡�ͬʱ��ÿ�� SELECT ����е��е�˳�������ͬ */
--ALL��ѡ��ʹ��ʱ����ȫ������ƥ��Ľ������Ȼ�����ؽ����ɾ������ƥ����ظ��У���ѯ���б������ڵ�һ����ѯ����ж���
--ALL�����ظ��У���������ʱ��order by
/*
SELECT dbo.Student.ClassNo AS '�༶�ż�ϵ��',dbo.Student.StuName AS ��ѧ������ʦ������ FROM dbo.Student
UNION 
SELECT dbo.Course.DeparNo,dbo.Course.Teacher FROM dbo.Course*/
/*�Ӳ�ѯ*/
/*�Ӳ�ѯ��һ��Ƕ����SELECT,INSERT,UPDATE,DELETE�������Ӳ�ѯ�еĲ�ѯ��Ҳ��һ��SELECT��䣬���ݲ�ѯ����������ͬ��Ϊ
���ض������ݵ��Ӳ�ѯ�ͷ��ص�ֵ���ݵ��Ӳ�ѯ���Ӳ�ѯҲ����Ƕ��ʹ��*/
/*���ض��е��Ӳ�ѯ*/
--�Ӳ�ѯ��λ��where�Ӿ��У�����IN��EXISTS�ؼ��ֺͱȽ����������
--1��ʹ��IN����Ԫ����Ŀ���е�ֵ���Ӳ�ѯ�ķ��ؽ�����бȽ�
--SELECT select_list FROM table_source [WHERE expression IN|NOT IN(subquery)]--subquery���Ӳ�ѯ
--SELECT dbo.Student.StuNo,dbo.Student.StuName,dbo.Student.ClassNo FROM dbo.Student,dbo.Score 
--WHERE dbo.Student.StuNo=dbo.Score.StuNo AND dbo.Score.Score>90
--SELECT dbo.Student.StuNo,dbo.Student.StuName,dbo.Student.ClassNo FROM dbo.Student
--WHERE dbo.Student.StuNo IN (SELECT StuNo FROM dbo.Score WHERE dbo.Score.Score>90)--���FROM����ֻ��һ����
--2��ʹ��EXIST,�÷���IN���ƣ�����������������Ϣ
--SELECT dbo.Student.StuNo,dbo.Student.StuName FROM dbo.Student WHERE NOT EXISTS --��IN ��ͬ������NOT EXISTSǰ�治�ø�StuNo
--(SELECT dbo.Score.StuNo FROM dbo.Score WHERE dbo.Student.StuNo=dbo.Score.StuNo )--�Ӳ�ѯ��һ��Ҫ��where����������
--3���Ƚ������
--SELECT select_list FROM table_source WHERE expression operator [ANY|SOME|ALL](subquery)
--operator��ʾ�Ƚ��������ANY|SOME��ʾ��Χ��ѯ�޶��������Ӳ�ѯ����ֵ���бȽϣ�����Χ��ѯ������������������Ƚ�
--��ȫ�����أ�ALL����Χ�Ӳ�ѯ���ؽ������ȫ������Ƚ�������
--SELECT dbo.Student.StuNo,ClassNo,StuName FROM dbo.Student,dbo.Score WHERE dbo.Score.Score < ANY --ֻҪ��һ����������������ʾ����
--(SELECT Score FROM dbo.Score WHERE dbo.Score.Score>90 )
--SELECT dbo.Student.StuNo,ClassNo,StuName FROM dbo.Student,dbo.Score WHERE dbo.Score.Score > ALL
--(SELECT StuNo FROM dbo.Score WHERE dbo.Score.Score>90)
/*���ص�ֵ���Ӳ�ѯ*/
--��ѯ���ֻ����һ��ֵ��Ȼ����Χ��ѯ��һ��ֵ��÷���ֵ�Ƚ�
--SELECT select_list FROM table_source WHERE expression operator (subquery)
--���ص�ֵ���Ӳ�ѯ�У��Ƚ����������Ҫʹ��ANY|SOME|ALL]
--SELECT StuNo,CouNo,Score FROM dbo.Score WHERE Score> (SELECT AVG(Score) FROM dbo.Score)
--/*Ƕ���Ӳ�ѯ*/
--һ���Ӳ�ѯ�����԰�������һ���Ӳ�ѯ
--SELECT dbo.Student.StuNo,StuName FROM dbo.Student,dbo.Score WHERE
 --Score=(SELECT MAX(Score) FROM dbo.Score GROUP BY CouNo)
 --��ѯ���ƿ����гɼ���ߵ�ѧ�ź�����
/*SELECT StuNo,StuName FROM dbo.Student 
WHERE StuNo=(SELECT StuNo FROM dbo.Score 
WHERE Score=(SELECT MAX(Score) FROM dbo.Score))*/
/*SELECT StuNo,StuName FROM dbo.Student --��ѯÿ����Ŀ�гɼ���ߵ�
WHERE StuNo IN (SELECT StuNo FROM dbo.Score 
WHERE Score IN (SELECT MAX(Score) FROM dbo.Score GROUP BY CouNo))*/

/*--INSERT���--*/
--�����������ݣ�һ���������Ӳ�ѯ����������һ�����
/*--1.INSERT VALUES���--*/
--INSERT [INTO] {<table name> | <view name>} [(<column name>[,{column name>}..)] 
--VALUES (<values>[,{<value>}..])
/*column nameָ�������ݱ����������ָ��һ�л���У�������Щ�б������'()'�С�ָ�������ʱ��,��������ָ����������
��ô��Ŀ�����ݱ��е�����δ��ָ�����б���֧�ֿ��ƻ�Ĭ��ֵ
VALUES�����ṩ����в����ֵ���������'()'�У�ָ�����ʱ��,����������������ӵ�һ�е�������ʱ����VALUES�������
���ݡ�INSERT����������еı�����ֻҪVALUES��������������CREATE TABLE ���������˳�򼴿ɡ�*/
USE jw
--INSERT INTO dbo.Course (CouNo,CouName,Credit,Teacher,DeparNo,Examkind) VALUES ('014','J2EE����','4.0','������','01','����')
/*--2.INSERT SELECT���--*/
--һ�β���һ�����ݣ���Щ���ݿ鶼�Ǵ���������Դѡ���õģ����ݿ��������ڣ����ݿ��е���һ����ͳһ���������������ݿ⣻
--��һ��sql��ѯ�����ͬһ������ĳЩ�н�����ѧ����õ��µ���ֵ��
--INSERT INTO <table name> SELECT column list FROM table list WHERE search conditions
--��SELECT�����Ľ����ΪINSERT�Ĳ���ֵ
/*ע�⣺������鱻�������еı��Ƿ������ݿ��У����뱣֤������ֵ�ı����е�����������ԭ����Ӧ�е���������һ�£�
������ȷ�����Ե����Ƿ����Ĭ��ֵ���ֵ�����������ֵ�������Ϊ��Щ���ṩֵ*/
--���Ƚ���һ���ձ�
/*USE jw
CREATE TABLE ClassBak--ClassBak�ձ������
(ClassN0 varchar(8) NOT NULL,DepartNo varchar(2) NOT NULL,ClassName varchar(20) NOT NULL)
--ͨ��INSERT SELECT��佫Class�е�Ԫ�����ClassBak��
USE jw
INSERT INTO ClassBak SELECT * FROM Class*/
/*--3.SELECT INTO����������--*/
--���԰��κβ�ѯ��������õ�һ���±��У������԰ѵ����������䵼���ݿ���±��С�
--SELECT <select_list> INTO new_table  FROM {<table_source>}
/*ע�⣺ʹ��SELECT INTOʱ���±��ܴ��������ݿ��У���������������Ϣ���±��е��к����ǻ��ڲ�ѯ�����*/
--���༶�����е����ݴ���һ����ʱ��ClassTemp
--USE jw
--SELECT * INTO ClassTemp FROM Class

/*--UPDATE���--*/
--�޸ı��е�����
--UPDATE <table name> SET <set clause expression> FROM table_name WHERE <search condition>
/*UPDATE��SET�Ǳ���ġ���UPDATE�Ӿ��У������ƶ�Ҫ���µı�����ơ�SET������һϵ����ֵ�ı��ʽ�����ʽ����������
�Ⱥź���ֵ��ɣ�˵��Ҫ���ĵ������ڹ�ϵ�е���λ�á�where��condition�����ƶ���Ҫ�޸ĵ������ڹ�ϵ�е���λ��*/
--USE jw
--UPDATE Score SET Score=Score+1 WHERE CouNo='001'
/*--����SELECT������ֵ--*/
/*USE jw--���ź�ϼ��ʦ����Ϣ����ϵ�������﹤��ϵ
UPDATE dbo.Course SET DepartNo=(SELECT DepartNo FROM dbo.Department WHERE DepartName='���﹤��ϵ' )
WHERE Teacher='�ź�ϼ'*/

/*--DELETE���--*/
--DELETE FROM <table name>[WHERE <searh condition>]--ֻ�ӱ���ɾ�����ݣ���ɾ�����屾������DROP TABLE�������屾��
--USE jw
--DELETE FROM Score WHERE CouNo='001'

/*--3.3 ���ݿ�������--*/
/*���ݿ����������������û������ݿ����ķ���Ȩ�ޣ��Լ�¼����ʽ�洢�ڸ������ݵ�sysprotectsϵͳ���У���Ϊ����״̬��
���裬�������ܾ�*/
--GRANT�������û�ĳЩȨ����ִ����صĲ��������ǽ�ɫ�������иý�ɫ�ĳ�Ա�̳д�Ȩ��
--REVOKE�����������Ȩ��
--DENY���ܾ��û�ִ��ĳЩ����
 /*--3.3.1 GRANT--*/
 --GRANT {ALL|statement} TO security_account
 --�����ɫpyp_role��Score��Ĳ��룬����Ȩ��
 --USE jw
 --GRANT INSERT,UPDATE on Score TO pyp_role
 /*--3.3.2 REVOKE--*/
 --USE jw--����
 --REVOKE INSERT,UPDATE ON Score FROM pyp_role
 /*--3.3.3 DENY--*/
 --��������Ȩ���Ժ����ݿ����Ա���Ը���ʵ������ڲ������û�����Ȩ�޵�����£�ʹ��DENY�ܾ��û��������ݿ����
 --USE jw
 -- DENY INSERT,UPDATE ON Score TO pyp_role
 --ʵ��
 --SELECT DepartName FROM dbo.Department WHERE DepartNo='01'
 --SELECT DepartName FROM dbo.Department WHERE DepartName like '%����%'
 --SELECT COUNT(ClassNo) FROM dbo.Class --
 /*SELECT dbo.Course.CouName,AVG(dbo.Score.Score) AS 'ƽ����' FROM dbo.Score,dbo.Course WHERE dbo.Score.CouNo= dbo.Course.CouNo 
 GROUP BY dbo.Course.CouNo,dbo.Course.CouName*/--���γ�ͳ�ƿγ̵�ƽ���֣���ʾ�γ����ƣ�ƽ����
 /*SELECT dbo.Department.DepartName,COUNT(dbo.Class.ClassName) FROM dbo.Department,dbo.Class WHERE dbo.Department.DepartNo=dbo.Class.DepartNo 
 GROUP BY dbo.Department.DepartNo,dbo.Department.DepartName--ͳ�Ƹ�ϵ�İ༶������ʾϵ��������༶��*/
 /*SELECT dbo.Student.StuNo,StuName FROM dbo.Student, dbo.Score WHERE dbo.Student.StuNo=dbo.Score.StuNo 
AND dbo.Score.Score>(SELECT AVG(dbo.Score.Score) FROM dbo.Score )*/--��ѯ�ɼ����ڿγ�ƽ���ֵ�ѧ����Ϣ
/*SELECT dbo.Course.CouName,dbo.Course.Credit,Score FROM dbo.Score INNER JOIN dbo.Student ON dbo.Student.StuNo=dbo.Score.StuNo 
INNER JOIN dbo.Course ON dbo.Score.CouNo=dbo.Course.CouNo
WHERE dbo.Student.StuName='��һƽ'*/--��ѯĳͬѧѡ�޵Ŀγ����ƣ�ѧ�֣��ɼ�������������
--DELETE FROM Student WHERE StuNo='0463501114'
/*UPDATE Score SET Score=81 WHERE StuNo=(SELECT StuNo from dbo.Student where StuName='�ⴺ') and 
CouNo=(SELECT CouNo from dbo.Course where CouName='���缼������' )*/--��ĳλͬѧ�ĳɼ��ĳ�81
/*--10!����
declare @i int,@sum int
set @i=1
set @sum=1
while @i<=10
begin 
set @sum=@sum*@i
set @i=@i+1
end 
print @sum */
--��ѯ����ǰ5�����5��ͬѧ�ɼ�
--select TOP 5 * FROM dbo.Score ORDER BY Score --Ĭ��Ϊ����
--select TOP 5 * FROM dbo.Score ORDER BY Score desc--����
