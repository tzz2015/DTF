import tornado


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')

    def result_format(self, data, msg='服务器错误', error_code=400):
        return self.write(result_format(data,msg,error_code))


# 登录验证 如果没有登录就返回统一格式
def login_required(func):
    def decorator(self, *args, **kwargs):
        if not self.current_user:
            return self.write(result_format(None, msg='用户没有登录', error_code=401))
        return func(self, *args, **kwargs)

    return decorator


def result_format(data, msg='服务器错误', error_code=400):
    r=''
    if data is None:
        r = {
            'code': error_code,
            'msg': msg,
            'data': None
        }
    else:
        r = {
            'code': 200,
            'msg': '操作成功',
            'data': data
        }
    print(r)
    return r
