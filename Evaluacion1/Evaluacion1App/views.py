from django.shortcuts import render

# Create your views here.

def Armas(request):
    return render(request, 'evaluacion1App/index.html')

def Espada(request):
    data = {
        "nombre" : "Espada",
        "desc" : "Esta muy afilada",
        "imagen" : "espada.png"
    }
    return render(request, 'evaluacion1App/pagina1.html', data)
def Escudo(request):
    data = {
        "nombre" : "Escudo",
        "desc" : "Me protege muy bien",
        "imagen" : "escudo.png"
    }
    return render(request, 'evaluacion1App/pagina1.html', data)
def Arco(request):
    data = {
        "nombre" : "Arco",
        "desc" : "Tengo buena punteria",
        "imagen" : "arco.png"
    }
    return render(request, 'evaluacion1App/pagina1.html', data)