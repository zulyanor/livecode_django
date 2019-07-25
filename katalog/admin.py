from django.contrib import admin
from .models import Barang

# Register your models here.
class BarangInput(admin.ModelAdmin):
    list_display = ['nama', 'gambar', 'harga', 'desc']

admin.site.register(Barang, BarangInput)