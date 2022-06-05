from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
# la función password determinará que es lo que se hará para generar la contraseña
def password(request):
    caracteres = list('abcdefghijklmnñopqrstuvwxyz') #ésta será la lista de caractéres con la que se generará la contraseña
    generadorpass = '' # la función generador recibirá los datos indicados en la selección que se haga de longitud
    length = int (request.GET.get('length')) # la variable length convertirá el request a un número entero con los métodos GET y get
    for x in range(length):
        generadorpass += random.choice(caracteres) #para la variable x generará una contraseña de acuerdo al rango que se obtenga de la variable length
    return render(request, 'password.html', {'contra': generadorpass}) #esto retornará la vista en el archivo html asignándole el nombre contra siendo que está recibirá el parámetro de la variable generador