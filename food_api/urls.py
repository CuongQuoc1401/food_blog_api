from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loai/<slug:slug>/', views.mon_an_theo_loai, name='mon_an_theo_loai'),
    path('mon-an/<slug:slug>/', views.chi_tiet_mon_an, name='chi_tiet_mon_an'),
    # Thêm các path khác cho vùng miền, tìm kiếm, v.v.
]