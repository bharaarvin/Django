from django.shortcuts import render
from . forms import Tamu
from . models import Guest

# Create your views here.

def tamu(request):
    buku_tamu = Tamu()

    context = {
        'BukuTamu': buku_tamu,
    }

    if request.method == "POST":
        Guest.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
            kegiatan = request.POST.get('kegiatan'),
        )

    return render(request, 'tamu/index.html', context)