from django.urls import path
from . import views

urlpatterns = [
    path('conversion/', views.logins, name='conversion'),
    #path('search_users', views.valid_user, name='search_users'),
    path('search_users', views.search_users, name='search_users'),

]
