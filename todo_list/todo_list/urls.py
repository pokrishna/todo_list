from django.contrib import admin
from django.urls import path,include
from todo_app import views
from todo_app.views import todo_listAPI
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("todo_app.urls")),
    # url("api/",views.todoDetailAPI.as_view()),
    # url("api/(?P<id>\d+)/",views.todoDetailAPI.as_view()),
    path("api/",todo_listAPI.as_view()),
]
