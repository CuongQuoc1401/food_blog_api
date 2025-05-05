from django.shortcuts import render, get_object_or_404
from .models import MonAn, LoaiMonAn

def home(request):
    mon_an_noi_bat = MonAn.objects.all().order_by('-luot_xem')[:8] # Lấy 8 món ăn có lượt xem cao nhất
    loai_mon_an = LoaiMonAn.objects.all()
    context = {
        'mon_an_noi_bat': mon_an_noi_bat,
        'loai_mon_an': loai_mon_an,
    }
    return render(request, 'food/home.html', context)

def mon_an_theo_loai(request, slug):
    loai = get_object_or_404(LoaiMonAn, slug=slug)
    mon_ans = loai.mon_ans.all() # Truy cập các món ăn liên quan thông qua related_name
    context = {
        'loai': loai,
        'mon_ans': mon_ans,
    }
    return render(request, 'food_api/mon_an_theo_loai.html', context)

def chi_tiet_mon_an(request, slug):
    mon_an = get_object_or_404(MonAn, slug=slug)
    mon_an.luot_xem += 1
    mon_an.save()
    context = {
        'mon_an': mon_an,
    }
    return render(request, 'food_api/chi_tiet_mon_an.html', context)

def monan_list(request):
    monan_list = MonAn.objects.all()
    loai_mon_ans = LoaiMonAn.objects.all()
    context = {
        'monan_list': monan_list,
        'loai_mon_ans': loai_mon_ans,
    }
    return render(request, 'food_api/monan_list.html', context)

def monan_detail(request, slug):
    mon_an = MonAn.objects.get(slug=slug)
    context = {
        'mon_an': mon_an,
    }
    return render(request, 'food_api/monan_detail.html', context)