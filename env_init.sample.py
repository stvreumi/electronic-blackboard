import pymysql
import subprocess
import bcrypt
import os

try:
    with open("mysql_auth.txt","r") as fp:
        host = fp.readline().rstrip()
        user = fp.readline().rstrip()
        passwd = fp.readline().rstrip()
        dbname = fp.readline().rstrip()
except:
    print("Open authorization file failed")
    exit(1)

print("Connect to MySQL server...")
try:
    client = pymysql.connect(host,user,passwd,use_unicode=True,charset="utf8")
    cursor = client.cursor()
except:
    print("Connect failed")
    exit(1)

print("Dropping database \"%s\" if existed..." % dbname)
cursor.execute("DROP DATABASE IF EXISTS "+dbname)
print("Creating database \"%s\"..." % dbname)
cursor.execute("CREATE DATABASE %s character set utf8" % dbname)
try:
    with open("create_tables.sql","r") as file:
        subprocess.call(["mysql","-u",user,"-p"+passwd],stdin=file)
except:
    print("Open sql file failed")
    exit(1)
client.close()

try:
    client = pymysql.connect(host,user,passwd,dbname,use_unicode=True,charset='utf8')
    cursor = client.cursor()
except:
    print("Connect failed")
    exit(1)

print("create user \"admin\"...")
user_name = 'admin'
user_hashed_passwd = bcrypt.hashpw('admin'.encode('utf-8'),bcrypt.gensalt())
try:
    ret = cursor.execute("insert into `user` (`user_name`,`user_password`,`user_level`) values (%s,%s,10000)", (user_name,user_hashed_passwd))
except:
    print("Insert user failed")

print("create data_type \"圖片\"...")
try:
    ret = cursor.execute('insert into `data_type` (`type_name`,`type_dir`) values ("圖片","圖片/")')
except:
    print("Insert type failed")

if not os.path.exists("static/圖片"):
    print("create dir \"圖片\"")
    os.makedirs("static/圖片")

print("create data_type \"獲獎公告\"...")
try:
    ret = cursor.execute('insert into `data_type` (`type_name`,`type_dir`) values ("獲獎公告","獲獎公告/")')
except:
    print("Insert type failed")

if not os.path.exists("static/獲獎公告"):
    print("create dir \"獲獎公告\"")
    os.makedirs("static/獲獎公告")

print("create data_type \"活動公告\"...")
try:
    ret = cursor.execute('insert into `data_type` (`type_name`,`type_dir`) values ("活動公告","活動公告/")')
except:
    print("Insert type failed")

if not os.path.exists("static/活動公告"):
    print("create dir \"活動公告\"")
    os.makedirs("static/活動公告")

print("create data_type \"氣像雲圖\"...")
try:
    ret = cursor.execute('insert into `data_type` (`type_name`,`type_dir`) values ("氣像雲圖","圖片/氣像雲圖/")')
except:
    print("Insert type failed")

if not os.path.exists("static/圖片/氣像雲圖"):
    print("create dir \"圖片/氣像雲圖\"")
    os.makedirs("static/圖片/氣像雲圖")

print("create data_type \"google日曆\"...")
try:
    ret = cursor.execute('insert into `data_type` (`type_name`,`type_dir`) values ("google日曆","google日曆/")')
except:
    print("Insert type failed")

if not os.path.exists("static/google日曆"):
    print("create dir \"/google日曆\"")
    os.makedirs("static/google日曆")

print("create arrage_mode 0...")
try:
    ret = cursor.execute('insert into `arrange_mode` (`armd_mode`) values (0)')
except:
    print("Insert arrange mode failed")

client.commit()
client.close()
