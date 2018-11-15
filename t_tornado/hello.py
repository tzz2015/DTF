import pymysql
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8002, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        db = pymysql.Connection(host='127.0.0.1', database='python_web', user='root', password='root1234',
                                charset='utf8')
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchall()
        print("Database version : %s " % data)
        db.commit()
        cursor.close()
        db.close()
        self.write('tornado 项目创建')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
