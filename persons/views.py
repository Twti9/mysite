from django.shortcuts import render
from django.http import HttpResponse
from persons.models import Blog,Author,Entry
# Create your views here.
def index(request):
    return HttpResponse('操作成功')