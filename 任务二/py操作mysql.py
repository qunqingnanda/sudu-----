import pymysql
# ---------------连接---------------------
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123321",
                     database="guanqing")
t_member=db.cursor()


# ------------删除--------------------------
sql_delect="delete from t_member where c_id=1"
t_member.execute(sql_delect)
db.commit()


# ------------清除所有-----------------------
clean="TRUNCATE TABLE t_member;"
t_member.execute(clean)
db.commit()


# ----------------------增加------------------
sql_add=" INSERT INTO t_member(c_id,c_name,c_stu_id,c_post,c_college,c_grade)VALUES(1,'超人强',2023123123,'技术组组长','计算机学院计科一班',100),(2,'GG bond',2023123124,'节目组编导','计算机学院计科二班',90),(3,'波比',2023123135,'技术组后端开发','电智学院电气一班',90);"
# 上面双引号内容为sql插入语句
t_member.execute(sql_add)
db.commit()


# ----------------------更新-------------------
sql_update = 'update t_member set c_name="喜羊羊" where c_name="超人强"'
t_member.execute(sql_update)
db.commit()

 
# -----------------查询(列）----------------(下面query的c_id可换，如c_name,c_post等）
query="SELECT c_id FROM t_member"
t_member.execute(query)
# ------------------print检查----------
result_query = t_member.fetchall()
for row in result_query:
    print(row)
print()


# -----------------批量查询------------
query_all = "SELECT * FROM t_member"
t_member.execute(query_all)
# -----------------print检查--------------
result_query_all = t_member.fetchall()
for row in result_query_all:
    print(row)


# ------------统计学生总数----------------
sql_count="SELECT COUNT(*) 学生人数总数  FROM t_member"
t_member.execute(sql_count)
result_count=t_member.fetchall()
for row in result_count:
    print(row)


# -------关闭----------------------------
if t_member:
    t_member.close()
db.close()
