from dataclasses import fields
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarroForm
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.

#class carroform(CarroForm):
#    class Meta:
#        model = carro
#        fields = ['modelo', 'marca', 'ano', 'valor', 'img']#, 'img'

def cadastro(request, template_name='cadastro.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, template_name, {'form': form})

def lista(request, template_name='lista.html'):
    Carro = carro.objects.all()
    carros = {'list': Carro}
    return render(request, template_name, carros)

def editar(request, id, template_name='editar.html'):
    Carro = carro.objects.get(id=id)
    form = CarroForm(request.POST, instance=Carro)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = CarroForm(instance=Carro)
    return render(request, template_name, {'Carro': Carro})

def deletar(request, id, template_name='deletar.html'):
    Carro = get_object_or_404(carro, id=id)
    if request.method == "POST":
        Carro.delete()
        return HttpResponseRedirect('/')
    return render(request, template_name, {'Carro':Carro})

def listar(request, template_name='lista.html'):
    query = request.GET.get("buscar")
    if query:
        Carro = carro.objects.filter(modelo__icontains=query)
    else:
        Carro = carro.objects.all()
    carros = {'list': Carro}
    return render(request, template_name, carros)