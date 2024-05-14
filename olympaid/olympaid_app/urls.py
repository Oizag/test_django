from django.urls import path
from . import views

app_name = 'olympaid'

urlpatterns = [
    path('', views.olympaid, name='olympaid'),
    path('register/', views.register, name='register'),
]
