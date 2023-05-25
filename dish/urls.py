from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dish.views import DishViewSet
from django.contrib import admin


urlpatterns = [

]


router = DefaultRouter()
router.register(r'dish', DishViewSet)

urlpatterns += router.urls
