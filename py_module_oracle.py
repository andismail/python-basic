PS:Mac OS
一、关于cx_Oracle
ps:python中使用oracle要用到cx_Oracle包，使用这个包前挺麻烦
ps:此处提到的oracle为11g，其它版本情况不知
ps:记录于2017-04-20

1.安装oracle的instantclient
	到oracle的官网下载: http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html ,不登陆还不让下载
	 instantclient-basic-macos.x64-11.2.0.4.0.zip
	 instantclient-sdk-macos.x64-11.2.0.4.0.zip
	 instantclient-sqlplus-macos.x64-11.2.0.4.0.zip
	其中的sqlplus文件好像是如果不用到sqlplus可以不用下
2.解压到某一个地方
	cd ~/Download
	mkdir 11
	mv instantclient-basic-macos.x64-11.2.0.4.0.zip instantclient-sdk-macos.x64-11.2.0.4.0.zip instantclient-sqlplus-macos.x64-11.2.0.4.0.zip ~/Download/11
	unzip instantclient-basic-macos.x64-11.2.0.4.0.zip
	unzip instantclient-sdk-macos.x64-11.2.0.4.0.zip
	unzip instantclient-sqlplus-macos.x64-11.2.0.4.0.zip
	解压第一个后会生成一个叫instantclient_11_2的文件夹，之后解压的两个都直接到了这个文件夹中
3.增加软链接
	cd instantclient_11_2
	ln -s libclntsh.dylib.11.1 libclntsh.dylib
	ln -s libocci.dylib.11.1 libocci.dylib
	不知道这两个有什么用，可能是提供给别的应用访问的
4.设置环境变量
	vim ~/.zshrc(bash的话是vim ~/.bash_profile)
	增加两个环境变量
	export ORACLE_HOME=/Users/Jthan/Downloads/11/instantclient_11_2
	export DYLD_LIBRARY_PATH=$ORACLE_HOME
	退出vim
	source ~/.zshrc
	环境变量这个东西在mac里也挺纠结,如果不编辑配置文件直接在控制台用命令，那么是只有当前的这个控制台有这个环境变量的
QA:若用到cx_Oracle的脚本要在集群中运行，那是不是集群中的服务器都要安装instantclient?
https://gist.github.com/rmoff/5a70862f27d2284e9541

二、一些sqlplus中的命令
1.连接
	a)登陆到装有Oracl的服务器
	b)su - oracle
		切换成功会看到命令行中有oracle字样如：[oracle@Z2krj5ecZ ~]$ 
	ps:实际情况是公司两台不同的服务器都可以连到oracle，不知原因
2.操作
	a)sqlplus /nolog
		切换到sqlplus操作,成功后如下
	SQL*Plus: Release 11.2.0.1.0 Production on Thu Apr 20 15:22:41 2017
	Copyright (c) 1982, 2009, Oracle.  All rights reserved.
	SQL> 
3.conn
	conn username/password
	意思好像是连接到某个用户,然后里面就都是这个用户的表,成功后如下显示
	Connected.
4.命令
	只用过mysql的我觉得sqlplus的格式化输出特别反人类，显示不全，结果被拆开，向上的方向键不支持
	set linesize 180
	set pages 999 #结果不被横线分开
	set long 90000 #结果显示全
	显示所有表:
	SELECT TABLE_NAME FROM DBA_TABLES; # 全有一大堆表，不知道都是些啥,可以用表名like
	显示建表语句:
	SELECT DBMS_METADATA.GET_DDL('TABLE','EAM_ACCOUNT_INFO') FROM DUAL;

三、cx_Oracle中的操作
import cx_Oracle
# 注掉这两种不知道为什么不好使，可以是因为没有建network/admin中的那个文件
#db = cx_Oracle.connect('hr', 'hrpwd', 'localhost:1521/XE')
#db1 = cx_Oracle.connect('hr/hrpwd@localhost:1521/XE')
dsnStr = cx_Oracle.makedsn("localhost", "1521", "orcl")
con = cx_Oracle.connect(user="eam", password="eam", dsn=dsnStr)
c = con.cursor()
#c.execute(u"SELECT DBMS_METADATA.GET_DDL('TABLE','EAM_ACCOUNT_INFO') FROM DUAL")
c.execute(u"SELECT 1 FROM DUAL")
for row in c:
	print(row)

四、数据恢复
	su - oracle
	impdp eam/eam directory=pump_dir dumpfile=路径/数据文件.dmp full=y
