from django.urls import path
from . import views

urlpatterns = [
    path('conversion/', views.logins, name='conversion'),
]
