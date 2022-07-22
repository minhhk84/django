from encodings import search_function
from django.contrib import admin
from .models import NguoiDung

# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ten_dang_nhap','email')
    list_filter = ('ten_dang_nhap','email')
    search_fields = ('ten_dang_nhap','email')
    list_per_page = 10

admin.site.register(NguoiDung, NguoiDungAdmin)
