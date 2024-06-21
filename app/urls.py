from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from catalogue import settings

urlpatterns = [
    path('', views.home, name=''),
    path('dashboard', views.dashboard, name='dashboard'),
    path('katalogbuku', views.katalogbuku, name='katalogbuku'),
    path('katalogpeta', views.katalogpeta, name='katalogpeta'),
    path('kataloganatomi', views.kataloganatomi, name='kataloganatomi'),
    path('katalogpaud', views.katalogpaud, name='katalogpaud'),
    path('katalogolahraga', views.katalogolahraga, name='katalogolahraga'),
    path('katalogmeubel', views.katalogmeubel, name='katalogmeubel'),
    path('katalogsd', views.katalogsd, name='katalogsd'),
    path('katalogsmp', views.katalogsmp, name='katalogsmp'),
    path('katalogsma', views.katalogsma, name='katalogsma'),
    path('detailbuku/<str:id>', views.detailproduk, name='detailbuku'),
    path('detailalat/<str:id>', views.detailalat, name='detailalat'),
    path('viewbuku', views.buku, name='viewbuku'),
    path('addbuku', views.addbuku, name='addbuku'),
    path('updatebuku/<str:id>', views.updatebuku, name='updatebuku'),
    path('delete/<str:id>', views.deletebuku, name='deletebuku'),
    path('viewalat', views.alat, name='viewalat'),
    path('addalat', views.addalat, name='addalat'),
    path('updatealat/<str:id>', views.updatealat, name='updatealat'),
    path('deletealat/<str:id>', views.deletealat, name='deletealat'),
    path('viewblog', views.blog, name='viewblog'),
    path('addblog', views.addblog, name='addblog'),
    path('updateblog/<str:id>', views.updateblog, name='updateblog'),
    path('deleteblog/<str:id>', views.deleteblog, name='deleteblog'),
]