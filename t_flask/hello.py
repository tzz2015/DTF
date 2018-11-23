import pymysql
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['get'])
def hello_world():
    searchword = request.args.get('key', '')
    db = pymysql.Connection(host='127.0.0.1', database='python_web', user='root', password='root1234', charset='utf8')
    try:
        cursor = db.cursor()
        sql_select = '''select * from auth_user'''
        cursor.execute(sql_select)
        data = cursor.fetchall()
        print(data)
        for row in data:
            id = row[0]
            psw = row[1]
            name = row[4]
            email = row[7]
            print('id=%s,name=%s,email=%s,psw=%s' % (id, name, email, psw))
        db.commit()
        cursor.close()
    except Exception as e:
        print('执行异常:%s' % e)
        db.rollback()
    db.close()

    return 'Flask 项目创建  %s' % searchword


if __name__ == '__main__':
    app.debug = True
    app.run(port=8001)
