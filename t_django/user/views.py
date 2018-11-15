from django.shortcuts import render
from django.http import HttpResponse
from user.utils import result_handler

# Create your views here.
def index(request):
    return result_handler("Django项目创建")
