from django.shortcuts import render, redirect
from .forms import *
from .models import *
import os
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):

    return render(request, 'index.html')

# Create your views here.
@login_required(login_url="/login")
def dashboard(request):

    return render(request, 'admin/dashboard.html')
    
def katalogbuku(request):
    buku = Buku.objects.all()

    return render(request, 'katalogbuku.html', {'buku':buku})

def katalogpeta(request):
    alat = PeralatanPendidikan.objects.filter(kategori="Peta")

    return render(request, 'katalogpeta.html', {'alat':alat})

def kataloganatomi(request):
    alat = PeralatanPendidikan.objects.filter(kategori="Anatomi")

    return render(request, 'kataloganatomi.html', {'alat':alat})

def katalogolahraga(request):
    alat = PeralatanPendidikan.objects.filter(kategori="Olahraga")

    return render(request, 'katalogolahraga.html', {'alat':alat})

def katalogmeubel(request):
    alat = PeralatanPendidikan.objects.filter(kategori="Meubel")

    return render(request, 'katalogmeubel.html', {'alat':alat})

def katalogpaud(request):
    alat = PeralatanPendidikan.objects.filter(kategori="PAUD")

    return render(request, 'katalogpaud.html', {'alat':alat})

def katalogsd(request):
    alat = PeralatanPendidikan.objects.filter(kategori="SD")

    return render(request, 'katalogsd.html', {'alat':alat})

def katalogsmp(request):
    alat = PeralatanPendidikan.objects.filter(kategori="SMP")

    return render(request, 'katalogsmp.html', {'alat':alat})

def katalogsma(request):
    alat = PeralatanPendidikan.objects.filter(kategori="SMA")

    return render(request, 'katalogsma.html', {'alat':alat})

def detailproduk(request,id):
    buku = Buku.objects.get(id_buku=id)

    return render(request, 'detailbuku.html', {'buku':buku})

def detailalat(request,id):
    alat = PeralatanPendidikan.objects.get(id_peralatan_pendidikan=id)

    return render(request, 'detailalat.html', {'alat':alat})

@login_required(login_url="/login")
def buku(request):
    buku = Buku.objects.all()

    return render(request, 'admin/viewbuku.html', {'buku':buku})

@login_required(login_url="/login")
def alat(request):
    alat = PeralatanPendidikan.objects.all()

    return render(request, 'admin/viewalat.html', {'alat':alat})

@login_required(login_url="/login")
def blog(request):
    blog = Blog.objects.all()

    return render(request, 'admin/viewblog.html', {'blog':blog})

@login_required(login_url="/login")
def addbuku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("viewbuku")
    else:
        form = BukuForm()

    return render(request, 'admin/addbuku.html')

@login_required(login_url="/login")
def addalat(request):
    if request.method == 'POST':
        form = AlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("viewalat")
    else:
        form = AlatForm()

    return render(request, 'admin/addalat.html')

@login_required(login_url="/login")
def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.penulis = "Admin"
            post.save()
            return redirect("viewblog")
    else:
        form = BlogForm()

    return render(request, 'admin/addblog.html')

@login_required(login_url="/login")
def updatebuku(request,id):
    buku = Buku.objects.get(id_buku=id)
    if request.method == "GET":
        return render(request, 'admin/updatebuku.html', {'buku':buku})
    
    else:
        if len(request.FILES) != 0:
            if len(buku.gambar) > 0:
                os.remove(buku.gambar.path)
            buku.gambar = request.FILES['gambar']
        buku.judul = request.POST['judul']
        buku.deskripsi = request.POST['deskripsi']
        buku.penerbit = request.POST['penerbit']
        buku.penulis = request.POST['penulis']
        buku.editor = request.POST['editor']
        buku.ukuran = request.POST['ukuran']
        buku.halaman = request.POST['halaman']
        buku.sinopsis = request.POST['sinopsis']
        buku.harga = request.POST['harga']
        buku.link = request.POST['link']
        buku.stok = request.POST['stok']
        buku.save()

        return redirect("viewbuku")

@login_required(login_url="/login")
def updatealat(request,id):
    alat = PeralatanPendidikan.objects.get(id_peralatan_pendidikan=id)
    if request.method == "GET":

        return render(request, 'admin/updatealat.html', {'alat':alat})
    else:
        if len(request.FILES) != 0:
            if len(alat.gambar) > 0:
                os.remove(alat.gambar.path)
            alat.gambar = request.FILES['gambar']
        alat.nama_peralatan = request.POST['nama_peralatan']
        alat.unit = request.POST['unit']
        alat.kategori = request.POST['kategori']
        alat.deskripsi = request.POST['deskripsi']
        alat.harga = request.POST['harga']
        alat.link = request.POST['link']
        alat.stok = request.POST['stok']
        alat.save()

        return redirect("viewalat")

@login_required(login_url="/login")
def updateblog(request,id):
    blog = Blog.objects.get(id_blog=id)
    tanggal = datetime.strftime(blog.tanggal, "%Y-%m-%d")
    if request.method == "GET":
        return render(request, 'admin/updateblog.html', {'blog':blog,'tanggal':tanggal})
    else:
        if len(request.FILES) != 0:
            if len(blog.gambar) > 0:
                os.remove(blog.gambar.path)
            blog.gambar = request.FILES['gambar']
        blog.judul = request.POST['judul']
        blog.deskripsi = request.POST['deskripsi']
        blog.tanggal = request.POST['tanggal']
        blog.kategori = request.POST['kategori']
        blog.save()

        return redirect("viewbuku")

@login_required(login_url="/login")
def deletebuku(request, id):
    buku = Buku.objects.get(id_buku=id)
    buku.delete()

    return redirect("viewbuku")

@login_required(login_url="/login")
def deletealat(request, id):
    alat = PeralatanPendidikan.objects.get(id_peralatan_pendidikan=id)
    alat.delete()

    return redirect("viewalat")

@login_required(login_url="/login")
def deleteblog(request, id):
    blog = Blog.objects.get(id_blog=id)
    blog.delete()

    return redirect("viewblog")
