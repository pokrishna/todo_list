
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from todo_app.views import todo_listAPI

urlpatterns = [
    path('',views.home,name="home"),
    path('update_list/(?P<id>\d+)/',views.update,name="update_list"),
    path('delete_list/<int:id>/',views.delete,name="delete_list"),

]
