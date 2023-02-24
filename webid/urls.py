from django.urls import path
from .import views
from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('registeruser/',views.registeruser, name='registeruser'),
    path('profile/',views.profile, name='profile'),
    path('status/',views.status, name='status'),
    path('doanloadidapp/',views.downloadidapp, name='downloadidapp'),
    path('importidforclaim/',views.importidforclaim, name='importidforclaim'),
    path('importidforclaimadmin/',views.importidforclaimadmin, name='importidforclaimadmin'),
    path('importdeptanddesignation/',views.importdeptanddesignation, name='importdeptanddesignation'),
    path('displayid/',views.displayid, name='displayid'),
    path('displayid/updateremarks/<int:id>', views.updateremarks, name='updateremarks'),
    path('displayid/searchidapplication', views.searchidapplication, name='searchidapplication'),
    path('displayid/updateremarks1/<int:id>', views.updateremarks1, name='update'),
    path('displayid/updateremarks1/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('displayid/refreshdata', views.refreshdata, name='refreshdata'),
    path('activeapplication/',views.activeapplication,name='activeapplication'),
    path('addid/',views.addid,name='addid'),
    path('downloadidadmin/',views.downloadidadmin,name='downloadidadmin'),
    
]