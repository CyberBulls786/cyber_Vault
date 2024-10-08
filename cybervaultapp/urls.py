from django.urls import path
from . import views

urlpatterns = [

    path('', views.index , name = 'index'),
    path('login/', views.user_login , name = 'login'),
    path('register/', views.register , name = 'register'),
    path('home/', views.main , name = 'home'),
    path('contact/', views.contactus , name = 'contact'),
    path('cybervault/', views.todo_list , name = 'todo_list'),
    path('cybervault/create', views.create_todo , name = 'create_todo'),
    path('blogs/', views.blogs , name = 'blogs'),

]

   

