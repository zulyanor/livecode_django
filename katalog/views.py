from django.shortcuts import render
from .models import Barang
from django.http import Http404
from .forms import InputBarang

# Create your views here.
def home(request):
    item = Barang.objects.all

    return render(request, 'home.html', {'item':item})

def barang(request, barang_id):
    try:
        item = Barang.objects.get(pk=barang_id)
    except Barang.DoesNotExist:
        raise Http404("Items does not exist")

    return render(request, 'barang_detail.html', {'item':item})

def input_barang(request):
    if request.method == "POST":
        form = InputBarang(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputBarang()
    
    return render(request, 'form_barang.html', {'form':form})