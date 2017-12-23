/*创建数据库*/
/*
CREATE DATABASE jw1
ON PRIMARY
(NAME=jw_data,
FILENAME='F:\AdventureWorksDW2008\jw_data.mdf',
SIZE=3MB,
MAXSIZE=5MB,--也可以没有
FILEGROWTH=1MB)
LOG ON 
(NAME=jw_log,
FILENAME='F:\AdventureWorksDW2008\jw_log.ldf',
SIZE=2MB,
MAXSIZE=5MB,
FILEGROWTH=10%
)--在该语句中， 创建了一个主数据文件jw_data.mdf和一个事务日志文件jw_log.ldf，数据文件初始大小是3，
最大容量是5，增值为1 */
/*5.2.2修改数据库*/
--创建添加文件组，增加或收缩数据库容量等
/*1. 创建文件组*/
--优势在于提高系统的性能：平衡多个磁盘的数据访问负荷；使用并行线程提高数据访问的效率；简化数据库维护，比如备份或
--恢复单个文件或文件组
--方式1，右击jw1，属性，文件组，添加，sencondary,确定，然后文件，添加，输入次要数据文件的名称：jw_data2，配置其他文件
--方式2，增加自定义文件组sencondary
/*ALTER DATABASE jw1
ADD FILEGROUP sencondary*/
--删除文件组
/*ALTER DATABASE jw1
REMOVE FILEGROUP sencondary*/
--将文件组设置为默认文件组或只读
/*ALTER DATABASE database_name
MODIFY FILEFROUP filegroup_name DEFAULT--DEFAULT默认，若改成READ_ONLY则是只读*/
/*2. 增加数据库容量*/
--1）创建数据库时设置数据库为自动增长方式
--2）属性，文件，修改文件初始大小与增长方式等
--3）使用ALTER,将jw.mdf的初始大小设置成5MB（初始大小修改只能变大）
/*ALTER DATABASE jw1
MODIFY FILE (NAME=jw_data,SIZE=5MB)*/
/*3. 收缩数据库容量*/
--1）设置为自动收缩方式。属性，选项，右边杂项，自动收缩将其值设置为True，确定
--2）右击数据库，任务，收缩，数据库
--3）将数据库大小收缩值5MB
--DBCC SHRINKDATABASE('jw1',5)
/*5.2.3 删除数据库*/
--1）略
--2） DROP DATABASE jw
/*5.3 数据库的分离和附加*/
/*分离数据库就是将某个数据库（如student_Mis）从SQL Server数据库列表中删除，使其不再被SQL Server管理和使用，
但该数据库的文件（.MDF）和对应的日志文件（.LDF）完好无损。分离成功后，我们就可以把该数据库文件（.MDF）和对应
的日志文件（.LDF）拷贝到其它磁盘中作为备份保存。
附加数据库就是将一个备份磁盘中的数据库文件（.MDF）和对应的日志文件（.LDF）拷贝到需要的计算机，并将其添加到
某个SQL Server数据库服务器中，由该服务器来管理和使用这个数据库。*/
--1)
--2)
--EXEC SP_DETACH_DB @dbname='jw1'--分离
--EXEC sp_attach_db @dbname=jw,@filename1='F:\AdventureWorksDW2008\jw.mdf'--附加
/*5.4 数据库的备份与还原*/
/*5.4.2 备份设备*/
--执行备份前需要创建备份设备，用来存储备份文件，备份设备包括：磁盘，磁带和命名管道等，这里是磁盘
--两种方式:在‘对象资源管理器’窗格中点击服务器名称，展开服务器树；展开‘服务器对象’，右击‘备份设备’；在弹出的快捷菜单
--中选择‘新建备份设备’，打开‘备份设备’窗口；在‘设备名称’中输入‘JWBACK’，‘目标’的‘文件’中设置路径，确定
--这里讲第二种
/*USE master
EXEC sp_addumpdevice 'disk','JWBACK','F:\AdventureWorksDW2008\JWBACK.bak'*/
/*5.4.3 创建数据库备份*/
/*图形化工具：展开服务器，‘数据库’节点，右击‘jw1’数据库，选择‘任务’中的‘备份’，打开‘备份数据库’窗口，在‘常规’
选项页中，‘数据库’选择‘jw1’，‘备份类型’选择‘完整’（原来是‘简单’，所以打开‘数据库属性’，选择‘选项’，选择‘恢复模式’
下的‘完整’），然后重新打开‘备份数据库’，设置备份到磁盘的目标位置，单击‘删除’，然后‘添加’按钮后，打开‘选择备份目标’
在‘备份设备’中选择‘JWBACK’，确定；然后‘选项’，点选‘覆盖所有现有备份集’，选中‘完成后验证备份’，确定
完成后，查看，‘对象资源管理器’，‘服务器对象’，‘备份设备’，右击‘JWBACK’，‘属性’，‘媒体内容’*/
--与BACKUP命令
/*
USE master
BACKUP DATABASE jw1
TO DISK='F:\AdventureWorksDW2008\JWBACK'
WITH INIT,--INIT表示‘覆盖所有备份集’，NOINIT表示‘追加到现有媒体集’
NAME='jw database backup',
DESCRIPTION='this is the full backup of jw1'*/
/*5.4.4 恢复数据库*/
--1.展开服务器，到‘数据库‘节点；右击’jw‘，’任务‘，‘还原’，‘数据库’，打开窗口，设置‘目标数据库’为‘jw'，
--’目标时间点‘可以设置为’最近状态‘，’还原的源‘用于指定源设备，打开’指定备份‘窗口，在‘备份媒体’中选择‘备份设备’，
--在‘备份位置’添加‘JWBACK'，确定。在‘还原数据库’的‘常规’中，选择用户还原的备份集。选项中，配置还原设置选项。
--使用RESTORE
/*
USE master
RESTORE DATABASE jw1 FROM JWBACK--设备
WITH FILE=1,--指从备份设备上第几个备份中恢复
NORECOVERY,--NORECOVERY,使数据库处于可用状态，RECOVERY处于不可用状态
REPLACE*/
/*5.5 数据库快照*/  
--是数据库的只读副本，在数据损坏的情况下，可以作为快速还原点，但不能替代备份，因为不包含数据中的所有记录
--1.没有图形用户界面，只有一种创建方式
/*
CREATE DATABASE JW_Data_1800--指定数据快照的名称
ON
(NAME=JW_Data,--指定数据库快照的稀疏文件的名称
FILENAME='F:\AdventureWorksDW2008\JW_Data_1800.SS')--路径
AS SNAPSHOT OF jw1--源数据库
*/
--2.使用数据库快照恢复数据库中的数据
--该方式只是简单的恢复机制，不应作为执行全面备份和还原策略的替代方案
--场景一 ，模拟灾难的发生，删除Class表中的数据
/*
DELETE FROM Class
--查看源数据库和快照中的数据，对比
USE jw
SELECT * FROM Class

USE JW_Data_1800
SELECT * FROM Class
--场景二：通过快照撤销Class表的删除
USE jw
GO
INSERT INTO Class
SELECT * FROM JW_Data_1800.abo.Class
--场景3，通过快照恢复Class表中的数据
USE jw
GO
RESTORE DATABASE jw FROM DATABASE_SNAPSHOT='JQ_Data_1800'
--场景二与三都可以
*/