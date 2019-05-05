
from django.urls import path
from api import views

urlpatterns = [
    path('task_lists', views.TaskListApiView.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    path('tasks', views.TaskApiView.as_view()),
    path('login', views.login)
]