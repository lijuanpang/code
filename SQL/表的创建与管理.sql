/*6.2.2用户自定义数据类型*/
--当多个表必须在一个列中存储相同类型的数据，而用户必须确保这些列具有相同的数据类型、长度和为空性时，
--可以使用用户自定义数据类型
--方式1：展开jw1的‘可编性’，‘类型’节点，右击后，‘新建’，‘用户数据类型’命令，在打开的‘新建用户定义数据类型’中的
--‘常规’中，设置架构为默认值dbo，名称中输入：StudentID;数据类型为：char;长度为8，确定
--方式2：
/*USE jw1
CREATE TYPE dbo.StudentID1 FROM char(8) NOT NULL*/
/*6.3.1创建、修改和删除表*/
--方式1,：不详细叙述。注意：表中可以设置某一字段自动编号，即插入数据时，不必赋值，系统自动给该字段排号
/*USE jw1
CREATE TABLE Student
(StuNo StudentID NOT NULL,
ClassNo char(8) NOT NULL,
StuName char(20) NOT NULL)*/
/*6.3.2修改表*/
--1.添加表字段，两种方式，设计 ，讲二
/*USE jw1
ALTER TABLE Student
ADD Birthday datetime NULL*/
--2.修改表字段
--两种方式，显示2
/*USE jw1
ALTER TABLE Student
ALTER COLUMN StuName varchar(30) NOT NULL*/
--3.删除表字段
--两种方式，第二种
/*USE jw1
ALTER TABLE dbo.Student
DROP COLUMN Birthday*/
/*6.3.3删除表*/
/*USE jw1
DROP TABLE dbo.Student*/
--以上是删除表，如果要保留表结构，仅删除表中数据，可以使用
--DELETE dbo.Student
--TRUNCATE TABLE dbo.Student
/*6.4 添加、修改和删除表中数据*/
--此外，INSERT,UPDATE,DELETE
/*
创建分区有四个步骤：选择分区列和分区边界值；创建分区函数，指定如何分区；创建分区方案，指定分区函数的分区在文件组
上的位置；创建使用分区方案的表，分割表*/

