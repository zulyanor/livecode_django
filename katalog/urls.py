from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barang/<int:barang_id>/', views.barang, name='barang_detail'),
    path('barang/input/', views.input_barang, name='input_barang')
]