from tornado.options import define, options
import pymysql
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from t_tornado.user import UserLogout, UserDelete, UserList, UserLogin, CreateUser

define("port", default=8002, help="run on the given port", type=int)
settings = {
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "http://localhost:8090/login",
}
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/login", UserLogin),
        (r"/userList", UserList),
        (r"/logout", UserLogout),
        (r'/createAndEdit', CreateUser),
        (r'/delete', UserDelete)
    ], debug=True, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

