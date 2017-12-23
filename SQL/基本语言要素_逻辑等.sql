/*
USE jw
--单行注释
/*这里是多行注释*/
SELECT * FROM dbo.Class --查询整个表格
*/

--声明局部变量

/*
DECLARE
{@local_variable [AS] data_type
| @cursor_variable_name CURSOR
}-- [ , ...n]
@local_variable 用于指定局部变量的名称，参数data_type用户设置局部变量的数据类型。
第二行是游标变量声明，@cursor_variable_name是游标变量名；[ , ...n]表示一个declare可以声明多个变量，
变量之间应用逗号隔开
DECLARE @a char(10),@b varchar(10) 
SELECT @a=2,@b=3
--SET @a=2 ,SET语句只能对单个变量赋值，SELECT可同时对多个；可以通过SELECT将查询结果赋值给某个变量
*/

--在本示例中使用

/*
DECLARE @Score decimal--声明一个浮点型的局部变量Score
SELECT @Score=85.0--赋值
USE jw
SELECT * FROM dbo.Score WHERE Score=@Score--查询
*/

--全局变量，可以被任何任何程序使用，通常存储配置设定值和统计数据，可用来测试系统的设定值胡执行T-SQL命令后的状态值

/*
--使用@@
--使用全局变量@@VERSION来查看当前使用的sql版本信息
SELECT @@VERSION
*/

--运算符

--用之执行算术运算，字符串连接运算符，赋值运算符，位运算符，比较运算符及逻辑运算等
/*
--1.算术运算符。+，-，*,/,%(取模)
--注意：除法，若两个表达式都是整数，那么结果只能取整数，小数值略去；取模运算，返回两数相除后的余数
SELECT 2.5+3.5
SELECT 2.5-3.5
SELECT 2.5*3.5'浮点型乘'
SELECT 2.5/3.5'浮点型除'
SELECT 2/3'整数除'
SELECT 2%3
*/
--2.赋值运算符，=，作用是赋值与查询（WHERE）
/*
--1)赋值
DECLARE @name varchar(20)
SET @name='崔梅华'
--2)查询
USE jw
SELECT * FROM dbo.Student WHERE StuName=@name
*/
--3位运算符。用于在二进制数据间执行位操作。&与，|或，^异或，当有一个为真时为1
/*
SELECT 1&0
SELECT 1&1
SELECT 1|0
SELECT 1^0
*/
--4.比较运算符，测试两个表达式是否相同=，>,<,>=,<=,!=(<>),!<(不小于)，!>
/*
USE jw
SELECT * FROM dbo.Score WHERE Score>=70.0
*/
--5.逻辑运算符，返回TRUE或FALSE，AND,OR,NOT,BETBEWWN,EXISTS,IN,LIKE,ALL,ANY,SOME
--EXISTS；如果子查询包含集合中某个元素，返回true
--IN；如果操作数包括集合中的某个元素
--LIKE；如果操作数与一种模式相匹配
--ALL；如果所有的都为true
/*
USE jw--查询学生表名字任意位置出现%春%，或姓朱的学生信息
SELECT * FROM dbo.Student WHERE StuName LIKE '%春%' OR StuName LIKE '朱%'--把*换成ClassNo，
*/
--6.字符串连接运算符，+
/*
USE jw
SELECT '学号：'+StuNo+'班级：'+ClassNo+'姓名：'+StuName FROM dbo.Student--使显示结果更方便阅读
*/

--函数；里面有内置函数也有自定义函数，下面将内置函数，四类

--行集函数：返回可在sql语句中像表引用一样使用的对象
--聚合函数：对一组值进行运算，但返回一个汇总值
--排名函数：对分区中的每一行均返回一个排名值
--标量函数：对单一值进行运算，然后返回单一值。只要表达式有效，即可使用标量函数
   --标量函数分为配置函数，游标函数，日期和时间函数等。
--1.日期函数。GETDATE()返回当前日期，而YEAR,MONTH,DAY,分别返回指定日期的年月日
/*
SELECT 
GETDATE() AS 当前日期,
YEAR(GETDATE()) AS 年,
MONTH(GETDATE()) AS 月,
DAY(GETDATE()) AS 日
*/
--2.聚合函数。AVG,MIN,MAX,SUM
--平均值
/*
USE jw
SELECT AVG(Score) AS '平均分' FROM Score 
SELECT MIN(Score) AS '最小值' FROM dbo.Score
*/
--3.排名函数。ROW_NUMBER()统计排名
/*
USE jw
SELECT StuNo,CouNo,Score,ROW_NUMBER() OVER (ORDER BY Score DESC) AS '排名' FROM dbo.Score--新加了一列排名
*/
--4.标量函数的使用，通过LTRIM()删除字符串变量中的起始空格
/*
DECLARE @string_to_ltrim varchar(30)
SET @string_to_ltrim='    HELLO WORLD'
SELECT @string_to_ltrim AS '原始字符'
SELECT LTRIM(@string_to_ltrim) AS '去掉起始空格'
*/

--流程控制语句 IF-ELSE,CASE,WHILE, GOTO,WAITFOR

--1.IF-ELSE 语句
/*
DECLARE @a int,@b int,@c int
SELECT @a=2,@b=3,@c=4
IF @a>@b
PRINT 'X>Y'
ELSE IF @b>@c
PRINT'Y>Z'
ELSE PRINT 'Z>Y'
*/
--2.begin with.while,case,if ...else,中若有多条语句，则需要用begin end将语句块包起来
--3.GO语句.GO语句不是T-SQL语句,两者不能再同一行
/*
USE jw
GO
DECLARE @MyMsg Varchar(50)
SELECT @MyMsg='HELLO WORLD'
GO
*/
--4.CASE 语句。可计算多个条件表达式，并将其中符合条件的结果表达式返回。分为简单CASE语句和搜索CASE语句
--1）简单case
/*
--不能运行
CASE sex
WHEN '1' THEN '男'
WHEN '0' THEN '女'
ELSE '其他'
end
CASE --搜索
WHEN sex='1' THEN '男'
WHEN sex='0' THEN '女'
ELSE '其他'
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
--5.WHILE..CONTINUE..BREAK语句
/*
DECLARE @INDEX INT=0,@ENDINDEX INT =0
WHILE @INDEX<5
	BEGIN
		SET @ENDINDEX=@ENDINDEX+1
		PRINT @ENDINDEX
		WHILE @ENDINDEX>5
			BEGIN 
				PRINT '防止死循环'
				BREAK--一旦进入循环到达break，那么跳出本循环,下面的也不循环,这个是死循环
			END
		CONTINUE--当IF语句不满足时，继续下一阶段
		SET @INDEX=@INDEX+1
	END
*/
--6.GOTO语句.将执行语句无条件跳转到标签处，并从标签处位置继续处理
/*8
DECLARE @x int
SELECT @x=0
label_1:
	SELECT @x=@x+1
	PRINT @x
	WHILE @x<6
GOTO label_1
*/
--7.WITHFOR 语句，延迟语句，用于设定在到达指定时间或时间间隔之前，两种表示方式
/*
USE jw
WAITFOR DELAY '01：02：03'--等待1小时2分3秒后执行SELECT语句
SELECT * FROM Student
--或
WAITFOR TIME '23：08：00'--等到1小时8分后才执行
SELECT * FROM Student
*/
--8.RETURN 语句；
--RETURN 语句用户从查询或过程中无条件退出。其之后的语句是不执行的，用于存储过程时，RETURN是不能返回控制的。
--若试图返回空值，则将生成警告消息并返回0 
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


