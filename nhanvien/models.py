from django.db import models

# Create your models here.
class NhanVien(models.Model):
    ten = models.CharField(max_length=100)
    tuoi = models.CharField(max_length=100)
    