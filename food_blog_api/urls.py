from django.contrib import admin
from django.urls import path, include

from food_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food_api.urls')), # Include URLs của app 'food' vào root URL
]