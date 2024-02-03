from django.urls import path
from . import views

urlpatterns=[
path('', views.home, name='home'),
path('register', views.register, name='register'),
path('login', views.my_login, name='my_login'),
path('logout', views.userLogOut, name='logout'),
path('dashboard', views.dashboard, name='dashboard'),
path('create_task', views.create_task, name='create_task'),
path('update_task/<int:pk>', views.update_task, name='update_task'),
path('singleTask/<int:pk>', views.singleTask, name='singleTask'),
path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    ]
