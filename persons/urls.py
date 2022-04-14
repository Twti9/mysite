#开发时间：2022/3/28 19:54
from django.urls import path
from . import views
app_name = 'person'

urlpatterns=[
    path('index/',views.index,name='index')
]
