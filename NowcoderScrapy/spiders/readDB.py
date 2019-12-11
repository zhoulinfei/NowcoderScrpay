import pymysql

connect = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='nowcoder', port=3306)
cursor = connect.cursor()
sql = "select content from javabycompany"
cursor.execute(sql)
result = cursor.fetchall()
text = ""
for r in result:
    text = text + "\n" + str(r[0])
filename = open("java.html", "w", encoding="utf-8")
filename.write(text)