import json

import pymysql
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8002, help="run on the given port", type=int)


class UserLogin(tornado.web.RequestHandler):
    def get(self):
        self.write(result_format(None, msg='此接口不支持GET请求'))

    def post(self, *args, **kwargs):
        json_result = json.loads(self.request.body)
        username = json_result.get('username')
        password = json_result.get('password')
        if username is None or username == '':
            self.write(result_format(None, msg='请输入用户名'))
        if password is None or password == '':
            self.write(result_format(None, msg='请输入用户密码'))

        db = pymysql.Connection(host='127.0.0.1', database='python_web', user='root', password='root1234',
                                charset='utf8')
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM user_sysuser WHERE username='%s' AND password='%s'" % (username, password))
            data = cursor.fetchone()
            db.commit()
            if data is not None:
                r = {
                    'id': data[0],
                    'username': data[1],
                    'email': data[3]
                }
                self.write(result_format(r))
            else:
                self.write(result_format(None, msg='登录失败'))
            cursor.close()
        except Exception as e:
            db.rollback()
            self.write(result_format(None, msg='登录异常:%s' % e))
        finally:
            db.close()


class UserList(tornado.web.RequestHandler):
    def get(self):
        db = pymysql.Connection(host='127.0.0.1', database='python_web', user='root', password='root1234',
                                charset='utf8')
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM user_sysuser")
            data = cursor.fetchall()
            db.commit()
            list = []
            for row in data:
                r = {
                    'id': row[0],
                    'username': row[1],
                    'email': row[3],
                    'create_time': row[4].strftime("%Y-%m-%d-%H %H:%M:%S")
                }
                list.append(r)
            self.write(result_format(list))
            cursor.close()
        except Exception as e:
            db.rollback()
            self.write(result_format(None, msg='%s' % e))
        finally:
            db.close()


class UserLogout(tornado.web.RequestHandler):
    def get(self):
        self.write(result_format(''))


class UserDelete(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id', 0)
        db = pymysql.Connection(host='127.0.0.1', database='python_web', user='root', password='root1234',
                                charset='utf8')
        try:
            cursor = db.cursor()
            row=cursor.execute("DELETE FROM user_sysuser WHERE id=%s" % id)
            db.commit()
            if row > 0:
                self.write(result_format(row))
            else:
                self.write(result_format(None, msg='删除失败'))
            cursor.close()
        except Exception as e:
            db.rollback()
            self.write(result_format(None, msg='%s' % e))
        finally:
            db.close()


class CreateUser(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        json_result = json.loads(self.request.body)
        username = json_result.get('username')
        password = json_result.get('password')
        email = json_result.get('email')
        db = pymysql.Connection(host='127.0.0.1', database='python_web', user='root', password='root1234',
                                charset='utf8')
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM user_sysuser WHERE username='%s'" % username)
            user = cursor.fetchone()
            if user is not None:
                self.write(result_format(None, msg='用户名已经存在'))
            else:
                row = cursor.execute(
                    "INSERT user_sysuser (username,password,email,create_time,update_time) VALUES ('%s','%s','%s',now(),now())" % (
                        username, password, email))
                self.write(result_format(row))
            db.commit()
            cursor.close()
        except Exception as e:
            db.rollback()
            self.write(result_format(None, msg='系统异常:%s' % e))
        finally:
            db.close()


def result_format(data, msg='服务器错误', error_code=400):
    if data is None:
        r = {
            'code': error_code,
            'msg': msg,
            'data': None
        }
        return r
    else:
        r = {
            'code': 200,
            'msg': '操作成功',
            'data': data
        }
        print(r)
        return r


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/login", UserLogin),
        (r"/userList", UserList),
        (r"/logout", UserLogout),
        (r'/createAndEdit', CreateUser),
        (r'/delete', UserDelete)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
