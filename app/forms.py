from django import forms
from .models import *

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ["gambar", "judul", "deskripsi", "penerbit", "penulis", "editor", "ukuran", "halaman","sinopsis", "harga", "link", "stok"]

class AlatForm(forms.ModelForm):
    class Meta:
        model = PeralatanPendidikan
        fields = ["gambar", "nama_peralatan", "unit", "kategori", "deskripsi", "harga", "link", "stok"]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["kategori", "tanggal", "judul", "deskripsi", "gambar"]
    