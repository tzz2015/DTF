from django.contrib.auth.models import User
from django.contrib import auth
import os
from user.model import UserInfo

os.environ['DJANGO_SETTINGS_MODULE'] = 't_django.t_django.settings'
import django


class UserService(object):
    # 用户登录验证
    def user_login(self, request, username, password):
        # 验证用户是否存在
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # 将用户信息保存到session中
            auth.login(request, user)
        return user

    # 退出登录
    def login_out(self, request):
        auth.logout(request)

    # 获取用户表
    def get_user_list(self):
        userList = []
        list = User.objects.all().filter(is_superuser=0)
        if list is not None:
            for item in list:
                userList.append(UserInfo(item).to_dict())
        return userList

    # 创建用户
    def create_user(self, username, password, email):
        if User.objects.filter(username=username):
            return '该用户名已经存在'
        else:
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.save()
            return None

    # 创建用户
    def edit_user(self, id,username,password,email):
        pass

    # 删除用户
    def delete_user(self,id):
        if not User.objects.filter(id=id):
            return '用户不存在'
        else:
            User.objects.filter(id=id).delete()



if __name__ == '__main__':
    django.setup()
    print(UserService.get_user_list())
