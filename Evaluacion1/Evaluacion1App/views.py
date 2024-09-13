from django.shortcuts import render

# Create your views here.

def Peliculas(request):
    return render(request, 'evaluacion1App/index.html')

def Batman1(request):
    data = {
        "nombre" : "Mascara del fantasma",
        "desc" : "Muy buena pelicula",
        "imagen" : "batman1.jpg"
    }
    return render(request, 'evaluacion1App/pagina1.html', data)

def Batman2(request):
    data = {
        "nombre" : "Gaslight",
        "desc" : "Mala pelicula",
        "imagen" : "batman2.jfif"
    }
    return render(request, 'evaluacion1App/pagina1.html', data)

def Batman3(request):
    data = {
        "nombre" : "Harley Quinn",
        "desc" : "Decente pelicula",
        "imagen" : "batman3.jpg"
    }
    return render(request, 'evaluacion1App/pagina1.html', data)