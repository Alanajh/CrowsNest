from django.urls import path, include
from . import views

urlpatterns = [
    path('login_users/', views.login_user, name="login"),   
    path('logout_users/', views.logout_user, name="logout"),   
]
