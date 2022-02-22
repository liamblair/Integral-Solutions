from django.urls import path

#from .views import RegisterView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
