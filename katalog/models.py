from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.CharField(max_length=20)
    gambar = models.CharField(max_length=255)
    desc = models.TextField()
