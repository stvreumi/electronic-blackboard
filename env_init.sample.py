import pymysql


with open("mysql_auth.txt","r") as fp:
    host = fp.readline().rstrip()
    user = fp.readline().rstrip()
    passwd = fp.readline().rstrip()
    dbname = fp.readline().rstrip()


print("Connect to MySQL server")
try:
    client = pymysql.connect(host,user,passwd,use_unicode=True,charset="utf8")
    cursor = client.cursor()
except:
    print("Connect failed")
    exit(1)

print("Dropping database \"%s\" if existed" % dbname)
cursor.execute("DROP DATABASE IF EXISTS "+dbname)
print("Creating database \"%s\"" % dbname)
cursor.execute("CREATE DATABASE %s" % dbname)

client.close()