from django.shortcuts import render

from dangky.models import NguoiDung

# Create your views here.

def dangky(request):
    return render(request,'dangky.html')

def trangchu(request):
    return render(request,'trangchu.html')

def xuly_dangky(request):
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    matkhau = request.GET.get('matkhau')

    if(len(ten)>3):
        data = NguoiDung(
            ten_dang_nhap = ten,
            email = mail,
            mat_khau = matkhau
        )
        data.save()
        return render(request,'dangnhap.html')
    else:
        return render(request,'loi.html')
    
