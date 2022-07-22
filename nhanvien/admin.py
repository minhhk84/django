from django.contrib import admin
from .models import NhanVien

# Register your models here.
class NhanVienAdmin(admin.ModelAdmin):
    list_display = ('ten','tuoi')

admin.site.register(NhanVien,NhanVienAdmin)
