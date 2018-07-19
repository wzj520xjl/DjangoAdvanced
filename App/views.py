import random

from django.core.paginator import Paginator
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
    page_num = int(request.GET.get('page',1))

    students = Student.objects.all()

    paginator = Paginator(students,10)

    page = paginator.page(page_num)

    data={
        'students':page.object_list,
        'page_object':page,
        'page_range':paginator.page_range,
    }

    return render(request,'student.html',context=data)