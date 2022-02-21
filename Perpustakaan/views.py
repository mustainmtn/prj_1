from django.shortcuts import render,redirect
from Perpustakaan.models import Buku
from Perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()
    konteks = {
        'books' : books,
    }
    return render(request, 'buku.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = FormBuku()
        pesan = "Data Berhasil Disimpan"
        konteks ={
            'form':form,
            'pesan':pesan,
        }
        return render(request,'tambah_buku.html',konteks)

    else:
        form = FormBuku()
        konteks = {
            'form' : form,
        }
        return render(request,'tambah_buku.html',konteks)


@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    if request.POST:
        form=FormBuku(request.POST,request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Diperbaharui')
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
                    'form':form,
                    'buku':buku,
                }
    return render(request,'ubah-buku.html',konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request,id_buku):
    buku=Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, 'Data Berhasil dihapus')
    return redirect('buku')


def daftar(request):
    if request.POST:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Berhasil Dibuat")
            return redirect('daftar')
        else:
            messages.error(request,"User Gagal Dibuat")
            return redirect('daftar')
    else:
        form=UserCreationForm()
        konteks = {
            'form':form,
        }
        return render(request,'daftar.html',konteks)
