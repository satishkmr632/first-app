from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^task/add/$', views.task_add, name='task_add'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit')
]