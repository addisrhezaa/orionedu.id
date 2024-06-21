from django.db import models
from django.utils.text import slugify

# Create your models here.
class Buku(models.Model):
    id_buku = models.SlugField(primary_key=True, max_length=255)
    gambar = models.ImageField()
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    penerbit = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    ukuran = models.CharField(max_length=50)
    halaman = models.IntegerField()
    sinopsis = models.TextField()
    harga = models.IntegerField()
    link = models.URLField()
    stok = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id_buku:
            self.id_buku = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul

class Blog(models.Model):
    id_blog = models.SlugField(primary_key=True, max_length=255)
    kategori = models.CharField(max_length=50)
    tanggal = models.DateField()
    penulis = models.CharField(max_length=100)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id_blog:
            self.id_blog = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul
    
class PeralatanPendidikan(models.Model):
    id_peralatan_pendidikan = models.SlugField(primary_key=True, max_length=255)
    gambar = models.ImageField()
    nama_peralatan = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    link = models.URLField()
    stok = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id_peralatan_pendidikan:
            self.id_peralatan_pendidikan = slugify(self.nama_peralatan)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama_peralatan