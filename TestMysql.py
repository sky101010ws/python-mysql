import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='mysql', charset='utf8')
    cur=conn.cursor()
    cur.execute('select host,user from user')
    data=cur.fetchall()
    for item in data:
        print("host:" + str(item[0]) + ", user:" + str(item[1]))

    cur.close()
    conn.close()
except Exception:print("error occur")
              
    
