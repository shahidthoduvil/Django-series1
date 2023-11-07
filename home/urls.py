from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home' ),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',register,name='register'),
    path('createpost/',PostCreate,name='createpost'),
    path('updatepost/<int:id>',Postupdate,name='updatepost'),
]
