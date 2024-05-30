from django.urls import path
from . import views

urlpatterns = [
    path('conversion/', views.logins, name='conversion'),
    path('search_users/', views.search_users, name='search-users'),
    path('create_account/', views.create_account, name='create-account'),
    path('main/', views.main, name='main'),
    ### Test query that must not be removed or commited ###
    path('accts/', views.accounts_list, name='acct-list'),
]
