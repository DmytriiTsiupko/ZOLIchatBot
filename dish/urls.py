from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dish.views import DishViewSet



urlpatterns = [

]


router = DefaultRouter()
router.register('', DishViewSet)

urlpatterns += router.urls
