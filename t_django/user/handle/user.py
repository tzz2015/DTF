from rest_framework.exceptions import APIException
from user.services.user import UserService
from django.http import HttpResponse
from user.utils import result_handler, login_required, check_null
from user.model import UserInfo
import json

from user.exception import Error

userService = UserService()


class UserHandler(object):
    # 用户登录
    def user_login(request):
        if request.method == 'POST':
            json_result = json.loads(request.body)
            username = json_result.get('username')
            password = json_result.get('password')
            if username is None:
                return result_handler(None, msg='请输入用户名')
            if password is None:
                return result_handler(None, msg='请输入密码')
            user = userService.user_login(request, username, password)
            if user is None:
                return result_handler(None, msg='用户名或者密码错误')
            return result_handler(UserInfo(user))

        else:  # 其他请求方式
            return result_handler('请使用POST请求')

    # 用户注销
    def login_out(request):
        userService.login_out(request)
        return result_handler('')

    # 用户列表
    @login_required
    def user_list(self):
        return result_handler(userService.get_user_list())

    # 创建用户和修改用户
    @login_required
    def createAndEdit(request):
        request_json = json.loads(request.body)
        id = request_json.get('id')
        username = request_json.get('username')
        password = request_json.get('password')
        email = request_json.get('email')
        if id is None:
            result = userService.create_user(username, password, email)
            if result:
                return result_handler(None, msg=result)
        else:
            userService.edit_user(id, username, password, email)

        return result_handler('')

    @login_required
    def delete_user(request):
        id = request.GET['id']
        if id:
            result = userService.delete_user(id)
            if result:
                return result_handler(None, msg=result)
        else:
            return result_handler(None, msg='用户id为空')
        return result_handler('')
