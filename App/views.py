import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def index(request):
    return HttpResponse('index')

def add_student(request):
    for i in range(10):
        s = Student()
        s.s_name = 'lele%d' % random.randrange(100)
        s.s_age = random.randrange(200)
        s.save()
    return HttpResponse('添加成功')


def get_student(request):
    return None