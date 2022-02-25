from django.urls import path

#From base folder (.) import views[.py]
from . import views

#Standard url pattern of "file path", "template/rendered image",
#and url name for Django purposes
urlpatterns = [
    path('register/', views.register, name='register'),
]
