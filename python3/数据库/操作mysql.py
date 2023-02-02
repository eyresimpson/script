# coding=utf-8
# !/usr/bin/python3

# 步骤1：导包（导入pymysql包）
# 步骤2：创建链接对象
# 步骤3：获取游标
# 步骤4：执行SQL
# 步骤5：关闭游标和链接
# 步骤6：分析结果

# Step1：导包
import pymysql

# Step2：获取链接
# 打开数据库连接
# connect/Connection和Connect都可以建立链接
db = pymysql.connect(host="localhost",  # 主机名
                     port=3306,  # 端口号
                     user="root",  # 用户名
                     password="root",  # 密码
                     database="mydb",  # 数据库名
                     charset="utf8")  # 编码格式

# Step3：获取游标
# 获取一个游标
cursor = db.cursor()

# Step4：执行SQL
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 构建SQL语句
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
# Step4：构建游标
cursor.execute(sql)

# Step5：关闭游标和链接
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
