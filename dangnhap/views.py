from django.shortcuts import render, get_object_or_404

from dangky.models import NguoiDung
# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')
    
    data = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = mk)
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung' : danh_sach
    }

    if data.exists():
        return render(request,'dangnhapthanhcong.html', context)
    else:
        return render(request,'loidangnhap.html')

def chi_tiet(request, nguoidung_id):
    nd = get_object_or_404(NguoiDung, pk = nguoidung_id)
    context = {
        'nguoi_dung':nd
    }
    return render(request, 'chitiet.html', context)

def xuly_capnhat(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')
    email = request.GET.get('mail')
    id_nd = request.GET.get('id_nd')
    
    NguoiDung.objects.filter(id = id_nd).update(
        ten_dang_nhap = ten,
        mat_khau = mk,
        email = email
    )

    return xuly_dangnhap(request)

def xoa_nguoidung(request, nguoidung_id):
    dulieu = get_object_or_404(NguoiDung,pk=nguoidung_id)
    try:
        dulieu.delete()
    except:
        print("Xoa bi loi")
    
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung': danh_sach
    }

    return render(request,'dangnhapthanhcong.html',context)