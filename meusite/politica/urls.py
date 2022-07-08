from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.index),
    path('politica', views.politica, name='politica.html'),
    url('chatbot', views.chatbot, name='chatbot'),
]