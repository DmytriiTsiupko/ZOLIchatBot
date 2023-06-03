from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes/', include('dish.urls')),
    path('users/', include('user.urls')),
    path('languages/', include('language.urls'))
]

