from django.shortcuts import render





def libros(request):
    return render(request, "core/nosotros.html")

def autor(request):
    return render(request, "core/autor.html")


def historias(request):
    return render(request, "core/historias.html")

def home(request):
    return render(request, "core/home.html")




















