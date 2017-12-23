--1.SELECT语句
/*
SELECT [ALL|DISTINCT] select_list
	[INTO new_table]
	FROM table_list
	[WHERE search_conditions]
	[GROUP BY group_by_list]
	[HAVING search_conditions]
	[ORDER BY order_list[ASC|DESC]]
	*/
--1.1基本查询
USE jw
--SELECT * FROM dbo.Class--获取表中所有的信息，并按照表中的顺序与格式进行排列
--SELECT ClassNo,ClassName FROM dbo.Class--获取表中指定的一列或几列数据
--SELECT ClassNo AS CN1,ClassName AS CN2 FROM dbo.Class--在返回结果中对列重命名，不改变表中的列名
--SELECT DISTINCT ClassNo,ClassName FROM dbo.Class--用DISTINCT 关键字删除重复行
--SELECT TOP 5 ClassNo,ClassName FROM dbo.Class--返回查询结果的行数，是表中自上向下的n行信息
--1.2 条件查询where
--SELECT * FROM dbo.Class WHERE ClassNo='20040001'--使用运算符
--SELECT * FROM dbo.Score WHERE Score>60 AND Score<80--使用逻辑运算符AND or
--SELECT * FROM dbo.Score WHERE NOT Score>60--使用NOT
/*IN条件，取值是否属于某一取值集合，IN 或NOT IN*/
--SELECT * FROM dbo.Class WHERE DepartNo IN ('01','02')--IN条件查询列表中各值都必须具有相同的数据类型
--SELECT * FROM dbo.Score WHERE Score BETWEEN '60' AND '80' /*BETWEEN 条件。某一范围，NOT BETWEEN*/
/*模糊查询。like与通配符 %：任意多个字符._:单个字符.[] 在指定范围内的单个字符.[^]：不在指定范围内的单个字符*/
--SELECT CouNo FROM dbo.Course WHERE Teacher LIKE '张%'--姓张的老师%
--SELECT CouNo FROM dbo.Course WHERE DeparNo like '0_',--使用无效_
--SELECT * FROM dbo.Course WHERE CouNo like '[01]%'--以0或1开头的所有课程信息
/*IS NOT NULL条件*/
--SELECT * FROM dbo.Course WHERE CouNo IS NOT NULL
--1.3.聚合与汇总GROUP BY,HAVING等
/*GROUP BY,可以对某一列数据的值进行分组*/--GROUP BY [ALL] <column>[,<column_name>...]ALL表示是否使用所有信息，常与where连用
--通常与聚合函数联合使用，SUM,AVG,MAX,MIN,COUNT(求组中项数，返回整数)
--SELECT CouNo,AVG(Score) AS '平均成绩' FROM dbo.Score GROUP BY CouNo  
--SELECT AVG(Score) AS '平均成绩' FROM dbo.Score WHERE CouNo='001'--该语句成立，总的平均，但是若SELECT后加一个 CouNo，就错了
--SELECT CouNo,AVG(Score) AS '平均成绩' FROM dbo.Score WHERE CouNo='001' GROUP BY CouNo--此时需要GROUP BY 
/*HAVING子句，与GROUP BY共同使用。WHERE用于限定每一行的查询条件，而HAVING用于限定分组统计值*/
--SELECT *FROM table WHERE search_condition1 GROUP BY column_name HAVING search_condition2
--SELECT CouNo,AVG(Score) AS '平均成绩' FROM dbo.Score WHERE CouNo LIKE '[01]%'  
--GROUP BY CouNo HAVING AVG(Score)>80
/*如果检索天剑需要在分组之前被应用，则用WHERE;而HAVING常用在GROUP BY之后，用以在结果集分组之后在进行判断
另外，聚合函数可以在SELECT与HAVING中使用，但不能再where中使用*/
/*ORDER BY */--一般用户SELECT语句最后，对查询返回的数据进行排序，正序逆序等
--ORDER BY order_expression[ASC|DESC]
/*order_expression致命拍序列的别名和表达式，当有多个排序列时，用逗号隔开，都可以跟排序要求，默认为升序ASC*/
--SELECT CouNo,AVG(Score) AS '平均成绩' FROM dbo.Score GROUP BY CouNo HAVING AVG(Score)>80 ORDER BY AVG(Score) DESC
--1.4多表查询 首先建立表之间的连接
--基本连接-笛卡尔乘积 两个表的每一行相乘，没什么用
--SELECT * FROM dbo.Score,dbo.Course
/*所以需要用WHERE给出条件，一般N个表有N-1个连接条件*/
--SELECT ClassNo,DepartName FROM dbo.Class,dbo.Department WHERE dbo.Class.DepartNo=dbo.Department.DepartNo
/*---内连接条件。
---SELECT中若列名在几个表中都存在，那么要注明基表名称；FROM包含所有使用到的基表名称；WHERE定义一个同等连接*/
--查询学号为0463501101的同学的名字，班级编号，名称及系编号与名称
/*
SELECT StuNo,StuName,dbo.Student.ClassNo,ClassName,dbo.Class.DepartNo,DepartName 
FROM dbo.Student,dbo.Class,dbo.Department
WHERE dbo.Student.ClassNo=dbo.Class.ClassNo AND dbo.Class.DepartNo=dbo.Department.DepartNo AND dbo.Student.StuNo='0463501101'
*/
---另一种连接语法形式是使用ANSI，用INNER JOIN进行连接查询（内连接中INNER可以省略），ON子句中给出连接条件
--SELECT select_list FROM table1 INNER JOIN table2[ON jion_condition] [WHERE search_conditions]
--查询学号为0463501101的同学的名字，班级编号，名称
--USE jw
--SELECT StuName,dbo.Student.ClassNo,ClassName FROM dbo.Student INNER JOIN dbo.Class ON dbo.Student.ClassNo=dbo.Class.ClassNo WHERE dbo.Student.StuNo=0463501101
/*内连接分为等值连接，自然连接和非等值连接*/
/*等值连接：使用=,结果中列出被连接表中的所有列，包括重复列*/
USE jw--学生信息及班级信息
--SELECT * FROM dbo.Student,dbo.Class WHERE dbo.Student.ClassNo= dbo.Class.ClassNo--结果中列ClassNo是重复的
--使用ANSI时
--SELECT * FROM dbo.Student INNER JOIN dbo.Class ON dbo.Student.ClassNo= dbo.Class.ClassNo--结果与上相同
/*自然连接：使用=，会删除重复列*/                 --把列一一列出
--SELECT StuNo,dbo.Student.ClassNo,StuName,DepartNo,ClassName FROM dbo.Student,dbo.Class WHERE dbo.Student.ClassNo= dbo.Class.ClassNo
/*非等值连接：不用=的<>等*/    
--SELECT dbo.Student.StuNo,StuName,CouNo,Score FROM dbo.Student,dbo.Score WHERE dbo.Student.StuNo=dbo.Score.StuNo AND Score>90
--SELECT dbo.Student.StuNo,StuName,CouNo,Score FROM dbo.Student INNER JOIN dbo.Score ON dbo.Student.StuNo=dbo.Score.StuNo WHERE Score>90
/*外连接*/
/*外连接：避免信息丢失，有主从表之分，以主表每行的数据去匹配从表中的数据行，若没有找到匹配行，主表的行依然保留并返回结果，相应的从表行被赋予NULL返回*/
/*分为左外连接，右外连接，全外连接*/
--左外连接： JOIN左边是主表，右边为从表
--SELECT select_list FROM table1 LEFT OUTER JOIN table2[ON jion_condition] [WHERE search_conditions]
--SELECT dbo.Course.CouNo,CouName,StuNo,Score FROM dbo.Course LEFT OUTER JOIN dbo.Score ON Course.CouNo=Score.CouNo AND Score>90
/*左外连接： JOIN右边是主表，左边为从表*/ --RIGHT OUTER JOIN
--SELECT CouNo,CouName,dbo.Department.DepartNo,DepartName FROM dbo.Course RIGHT OUTER JOIN dbo.Department ON dbo.Course.DeparNo=dbo.Department.DepartNo
/*全外连接，都返回*/ --FULL OUTER JOIN
--SELECT dbo.Student.StuNo,StuName,CouNo,Score FROM dbo.Student FULL OUTER JOIN dbo.Score ON dbo.Student.StuNo=dbo.Score.StuNo
/*注意：on与where区别，1、 on条件是在生成临时表时使用的条件，它不管on中的条件是否为真，都会返回左边表中的记录。*/
--2、where条件是在临时表生成好后，再对临时表进行过滤的条件。这时已经没有left join的含义（必须返回左边表的记录）了，条件不为真的就全部过滤掉。
/*交叉连接*/
/*如果交叉连接不带where子句，则返回的结果是被连接的两个表的笛卡尔乘积；如果带，则是两个表的笛卡尔乘积减去where所限定而省略的行数*/
--SELECT select_list FROM table CROSS JOIN table [WHERE search_conditions]
USE jw
--SELECT * FROM dbo.Class CROSS JOIN dbo.Department--和，的效果一样
/*自连接*/
--自己连接自己查询，比如是课程相同，教师不同的课程信息，
--SELECT t1.CouNo,t1.CouName,t1.Teacher FROM Course t1,Course t2 WHERE t1.CouName=t2.CouName AND t1.Teacher !=t2.Teacher
--以上查询时将Course表建立了两个别名t1，t2，用于对两个吧IAO进行连接查询
/*联合连接*/
--将不同的查询结果纵向依次连接，
/*
SELECT select_list FROM table_source [WHERE search_condition]
{UNION[ALL]
SELECT select_list FROM table_source [WHERE search_condition] }  [ORDER BY order_expression]
UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同 */
--ALL可选，使用时返回全部满足匹配的结果，不然，返回结果中删除满足匹配的重复行，查询的列表是需在第一个查询语句中定义
--ALL允许重复列，重新排列时用order by
/*
SELECT dbo.Student.ClassNo AS '班级号及系好',dbo.Student.StuName AS ‘学生及教师姓名’ FROM dbo.Student
UNION 
SELECT dbo.Course.DeparNo,dbo.Course.Teacher FROM dbo.Course*/
/*子查询*/
/*子查询是一个嵌套在SELECT,INSERT,UPDATE,DELETE或其他子查询中的查询，也是一条SELECT语句，根据查询返回行数不同分为
返回多行数据的子查询和返回单值数据的子查询，子查询也可以嵌套使用*/
/*返回多行的子查询*/
--子查询都位于where子句中，并与IN，EXISTS关键字和比较运算符想结合
--1）使用IN，将元彪中目标列的值和子查询的返回结果进行比较
--SELECT select_list FROM table_source [WHERE expression IN|NOT IN(subquery)]--subquery是子查询
--SELECT dbo.Student.StuNo,dbo.Student.StuName,dbo.Student.ClassNo FROM dbo.Student,dbo.Score 
--WHERE dbo.Student.StuNo=dbo.Score.StuNo AND dbo.Score.Score>90
--SELECT dbo.Student.StuNo,dbo.Student.StuName,dbo.Student.ClassNo FROM dbo.Student
--WHERE dbo.Student.StuNo IN (SELECT StuNo FROM dbo.Score WHERE dbo.Score.Score>90)--这里，FROM后面只有一个表
--2）使用EXIST,用法与IN相似，返回满足条件的信息
--SELECT dbo.Student.StuNo,dbo.Student.StuName FROM dbo.Student WHERE NOT EXISTS --与IN 不同的是在NOT EXISTS前面不用跟StuNo
--(SELECT dbo.Score.StuNo FROM dbo.Score WHERE dbo.Student.StuNo=dbo.Score.StuNo )--子查询中一定要有where连接两个表
--3）比较运算符
--SELECT select_list FROM table_source WHERE expression operator [ANY|SOME|ALL](subquery)
--operator表示比较运算符；ANY|SOME表示外围查询限定条件与子查询返回值进行比较，若外围查询中有任意多个数据满足比较
--则全部返回；ALL，外围子查询返回结果必须全部满足比较条件。
--SELECT dbo.Student.StuNo,ClassNo,StuName FROM dbo.Student,dbo.Score WHERE dbo.Score.Score < ANY --只要有一个满足条件，都显示出来
--(SELECT Score FROM dbo.Score WHERE dbo.Score.Score>90 )
--SELECT dbo.Student.StuNo,ClassNo,StuName FROM dbo.Student,dbo.Score WHERE dbo.Score.Score > ALL
--(SELECT StuNo FROM dbo.Score WHERE dbo.Score.Score>90)
/*返回单值的子查询*/
--查询结果只返回一个值，然后外围查询将一列值与该返回值比较
--SELECT select_list FROM table_source WHERE expression operator (subquery)
--返回单值的子查询中，比较运算符不需要使用ANY|SOME|ALL]
--SELECT StuNo,CouNo,Score FROM dbo.Score WHERE Score> (SELECT AVG(Score) FROM dbo.Score)
--/*嵌套子查询*/
--一个子查询还可以包含着另一个子查询
--SELECT dbo.Student.StuNo,StuName FROM dbo.Student,dbo.Score WHERE
 --Score=(SELECT MAX(Score) FROM dbo.Score GROUP BY CouNo)
 --查询各科考试中成绩最高的学号和姓名
/*SELECT StuNo,StuName FROM dbo.Student 
WHERE StuNo=(SELECT StuNo FROM dbo.Score 
WHERE Score=(SELECT MAX(Score) FROM dbo.Score))*/
/*SELECT StuNo,StuName FROM dbo.Student --查询每个科目中成绩最高的
WHERE StuNo IN (SELECT StuNo FROM dbo.Score 
WHERE Score IN (SELECT MAX(Score) FROM dbo.Score GROUP BY CouNo))*/

/*--INSERT语句--*/
--向表中添加数据，一条或利用子查询将整块数据一起插入
/*--1.INSERT VALUES语句--*/
--INSERT [INTO] {<table name> | <view name>} [(<column name>[,{column name>}..)] 
--VALUES (<values>[,{<value>}..])
/*column name指定该数据表的列名，可指定一列或多列，所有这些列必须放在'()'中。指定多个列时用,隔开。若指定了列名，
那么在目标数据表中的所有未被指定的列必须支持控制或默认值
VALUES用于提供向表中插入的值，必须放在'()'中，指定多个时用,隔开；当将数据添加到一行的所有列时，用VALUES给出添加
数据。INSERT无需给出表中的别名，只要VALUES给出的数据与用CREATE TABLE 定义给出的顺序即可。*/
USE jw
--INSERT INTO dbo.Course (CouNo,CouName,Credit,Teacher,DeparNo,Examkind) VALUES ('014','J2EE开发','4.0','王建军','01','考察')
/*--2.INSERT SELECT语句--*/
--一次插入一块数据，这些数据块都是从其他数据源选择获得的，数据可能来自于：数据库中的另一个表；统一服务器上其他数据库；
--另一个sql查询结果；同一个表（对某些列进行数学运算得到新的列值）
--INSERT INTO <table name> SELECT column list FROM table list WHERE search conditions
--由SELECT产生的结果集为INSERT的插入值
/*注意：必须检验被插入新行的表是否在数据库中；必须保证接受新值的表中列的数据类型与原表相应列的数据类型一致；
必须明确被忽略的列是否存在默认值或空值，若不允许空值，则必须为这些列提供值*/
--首先建立一个空表
/*USE jw
CREATE TABLE ClassBak--ClassBak空表的名字
(ClassN0 varchar(8) NOT NULL,DepartNo varchar(2) NOT NULL,ClassName varchar(20) NOT NULL)
--通过INSERT SELECT语句将Class中的元组插入ClassBak中
USE jw
INSERT INTO ClassBak SELECT * FROM Class*/
/*--3.SELECT INTO语句插入数据--*/
--可以把任何查询结果集放置到一个新表中，还可以把导入的数据填充导数据库的新表中。
--SELECT <select_list> INTO new_table  FROM {<table_source>}
/*注意：使用SELECT INTO时，新表不能存在于数据库中，否则会产生错误信息；新表中的行和列是基于查询结果的*/
--将班级中所有的数据存在一张临时表ClassTemp
--USE jw
--SELECT * INTO ClassTemp FROM Class

/*--UPDATE语句--*/
--修改表中的数据
--UPDATE <table name> SET <set clause expression> FROM table_name WHERE <search condition>
/*UPDATE与SET是必须的。在UPDATE子句中，必须制定要更新的表的名称。SET后面是一系列新值的表达式，表达式由属性名、
等号和新值组成，说明要更改的数据在关系中的列位置。where的condition条件制定将要修改的数据在关系中的行位置*/
--USE jw
--UPDATE Score SET Score=Score+1 WHERE CouNo='001'
/*--利用SELECT语句更新值--*/
/*USE jw--将张红霞老师从信息工程系调到生物工程系
UPDATE dbo.Course SET DepartNo=(SELECT DepartNo FROM dbo.Department WHERE DepartName='生物工程系' )
WHERE Teacher='张红霞'*/

/*--DELETE语句--*/
--DELETE FROM <table name>[WHERE <searh condition>]--只从表中删除数据，不删除表定义本身，可用DROP TABLE产出表定义本身
--USE jw
--DELETE FROM Score WHERE CouNo='001'

/*--3.3 数据控制语言--*/
/*数据控制语言用来设置用户对数据库对象的访问权限，以记录的形式存储在各个数据的sysprotects系统表中，分为三种状态：
授予，撤销，拒绝*/
--GRANT：授予用户某些权限以执行相关的操作，若是角色，则所有该角色的成员继承此权限
--REVOKE：撤销授予的权限
--DENY：拒绝用户执行某些操作
 /*--3.3.1 GRANT--*/
 --GRANT {ALL|statement} TO security_account
 --授予角色pyp_role对Score表的插入，更新权限
 --USE jw
 --GRANT INSERT,UPDATE on Score TO pyp_role
 /*--3.3.2 REVOKE--*/
 --USE jw--撤销
 --REVOKE INSERT,UPDATE ON Score FROM pyp_role
 /*--3.3.3 DENY--*/
 --在授予了权限以后，数据库管理员可以根据实际情况在不撤销用户访问权限的情况下，使用DENY拒绝用户访问数据库对象
 --USE jw
 -- DENY INSERT,UPDATE ON Score TO pyp_role
 --实验
 --SELECT DepartName FROM dbo.Department WHERE DepartNo='01'
 --SELECT DepartName FROM dbo.Department WHERE DepartName like '%工程%'
 --SELECT COUNT(ClassNo) FROM dbo.Class --
 /*SELECT dbo.Course.CouName,AVG(dbo.Score.Score) AS '平均分' FROM dbo.Score,dbo.Course WHERE dbo.Score.CouNo= dbo.Course.CouNo 
 GROUP BY dbo.Course.CouNo,dbo.Course.CouName*/--按课程统计课程的平均分，显示课程名称，平均分
 /*SELECT dbo.Department.DepartName,COUNT(dbo.Class.ClassName) FROM dbo.Department,dbo.Class WHERE dbo.Department.DepartNo=dbo.Class.DepartNo 
 GROUP BY dbo.Department.DepartNo,dbo.Department.DepartName--统计各系的班级数，显示系部名称与班级数*/
 /*SELECT dbo.Student.StuNo,StuName FROM dbo.Student, dbo.Score WHERE dbo.Student.StuNo=dbo.Score.StuNo 
AND dbo.Score.Score>(SELECT AVG(dbo.Score.Score) FROM dbo.Score )*/--查询成绩高于课程平均分的学生信息
/*SELECT dbo.Course.CouName,dbo.Course.Credit,Score FROM dbo.Score INNER JOIN dbo.Student ON dbo.Student.StuNo=dbo.Score.StuNo 
INNER JOIN dbo.Course ON dbo.Score.CouNo=dbo.Course.CouNo
WHERE dbo.Student.StuName='葛一平'*/--查询某同学选修的课程名称，学分，成绩，连接三个表
--DELETE FROM Student WHERE StuNo='0463501114'
/*UPDATE Score SET Score=81 WHERE StuNo=(SELECT StuNo from dbo.Student where StuName='吴春') and 
CouNo=(SELECT CouNo from dbo.Course where CouName='网络技术基础' )*/--将某位同学的成绩改成81
/*--10!计算
declare @i int,@sum int
set @i=1
set @sum=1
while @i<=10
begin 
set @sum=@sum*@i
set @i=@i+1
end 
print @sum */
--查询排名前5名与后5名同学成绩
--select TOP 5 * FROM dbo.Score ORDER BY Score --默认为升序
--select TOP 5 * FROM dbo.Score ORDER BY Score desc--降序
