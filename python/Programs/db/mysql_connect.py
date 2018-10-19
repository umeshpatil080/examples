import pymysql

try:
    conn = pymysql.connect(host='localhost', port=4002, user='root', passwd='123', db='mysql')
    cur = conn.cursor()
    cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    print()
    for row in cur:
        print(row)
    cur.close()
    conn.close()
except Exception as e:
    print("Error:" + str(e))