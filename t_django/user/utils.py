from django.http import HttpResponse
import json
from django.core import serializers


# 统一返回格式
def result_handler(data, msg='not found', errcode=400):
    model = BaseModel(data, msg, errcode)
    print(model.to_dict())
    return HttpResponse(json.dumps(model.to_dict()), content_type="application/json")


# 登录验证 如果没有登录就返回统一格式
def login_required(func):
    def decorator(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return result_handler(None, msg='用户没有登录', errcode=401)
        return func(request, *args, **kwargs)

    return decorator


class BaseModel(object):
    def __init__(self, data, msg='not found', errcode=400):
        if data is None:
            self.code = errcode
            self.data = data,
            self.msg = msg
        else:
            if isinstance(data, str) or isinstance(data, list):
                self.code = 200
                self.data = data
                self.msg = 'ok'
            else:
                self.code = 200
                self.data = data.to_dict()
                self.msg = 'ok'

    def to_dict(self):
        r = {
            'code': self.code,
            'data': self.data,
            'msg': self.msg
        }
        return r


def check_null(value, msg=''):
    if value is None or value == '':
        return result_handler(None, msg='%s不能为空' % msg)
