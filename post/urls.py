from django.urls import path,include
from .import views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('user/',views.users,name = 'users'),
    path('users/<id>/',views.usersingle,name = 'usersingle'),
    path('message/<id>/',views.message,name = 'message'),
    path('edit/<id>/',views.edit,name = 'edit'),
    path('delete/<id>/',views.delete,name = 'delete'),
    path('liked/<id>/',views.liked,name = 'likes'),
    path('crud_ajax/', views.crud_ajax_create,name='crud_ajax_create'),
]
