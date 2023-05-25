from django.urls import path
from . import views

app_name = 'dish'

urlpatterns = [
    path('', views.index, name='dishes'),
]