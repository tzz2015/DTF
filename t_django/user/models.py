from django.db import models


# Create your models here.
class SysUser(models.Model):
    username = models.CharField(max_length=16)
    password=models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now=True)

