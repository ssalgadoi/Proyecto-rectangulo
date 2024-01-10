from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('historias/',views.historias, name="historias"),
    path('autor/', views.autor, name="autor"),
    path('nosotros/',views.libros, name="nosotros"),
]