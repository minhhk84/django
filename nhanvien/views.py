from django.shortcuts import render

from nhanvien.models import NhanVien

# Create your views here.
def nhanvien(request):
    return render(request, 'nhanvien.html')

def xuly_nhanvien(request):
    ten = request.GET.get('ten')
    tuoi = request.GET.get('tuoi')

    data = NhanVien.objects.filter(ten = ten)
    if data.exists():
        return render(request,'khongthanhcong.html')
    else:
        data = NhanVien(
            ten = ten,
            tuoi = tuoi
        )
        data.save()
        return render(request,'thanhcong.html')