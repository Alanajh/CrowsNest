from django.urls import path
from . import views

urlpatterns = [
    path('login_users/', views.login_user, name="login"),   
    path('logout_users/', views.logout_user, name="logout"),  
    path('create_user/', views.create_user, name="create-user"),    
    path('querySet_build/', views.querySet_build, name="querySet_build"),   
]
