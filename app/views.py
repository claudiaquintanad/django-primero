from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse(f'<h2>placeholder para luego mostrar una lista de todos los blogs<h2>')
def new(request):
    return HttpResponse(f'<p>placeholder para mostrar un nuevo formulario para crear un nuevo blog con un método llamado "new"<p>')
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'<h1>placeholder para mostrar el blog numero {number}</h1>')
def edit(request, number):
    return HttpResponse(f'<h1>placeholder para editar el blog {number}" con un método llamado "edit"</h1>')
def destroy(request, number):
    return redirect('/blogs')
def jres(request):
    data = [{'titulo': 'Blog', 'num_blog': '1'}, {'titulo': 'parrafos', 'num_parrafo': '5'}]
    return JsonResponse({'data': data})
