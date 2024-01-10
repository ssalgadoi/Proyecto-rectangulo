from django.shortcuts import render
from .forms import ContactoForm


# Create your views here.
def contact(request):
    
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
    return render(request, "contact/contacto.html", data)