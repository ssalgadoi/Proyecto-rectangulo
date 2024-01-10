from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="noticias"),
    path('category/<int:category_id>/', views.category, name="category"),
]