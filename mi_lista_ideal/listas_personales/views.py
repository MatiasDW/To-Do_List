from django.shortcuts import render, get_object_or_404, redirect
from .models import Lista, Tarjeta, Tablero
from .forms import ListaForm, TarjetaForm, TableroForm

def lista_todas(request):
    listas = Lista.objects.all()
    return render(request, 'listas/listas.html', {'listas': listas})

def lista_detail(request, pk):
    lista = get_object_or_404(Lista, pk=pk)
    return render(request, 'listas/lista_detail.html', {'lista': lista})

def lista_nueva(request):
    if request.method == "POST":
        form = ListaForm(request.POST)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.author = request.user
            lista.save()
            return redirect('lista_detail', pk=lista.pk)
    else:
        form = ListaForm()
    return render(request, 'listas/lista_form.html', {'form': form})

def tarjeta_detail(request, pk):
    tarjeta = get_object_or_404(Tarjeta, pk=pk)
    return render(request, 'tarjetas/tarjeta_detail.html', {'tarjeta': tarjeta})

def tarjeta_nueva(request):
    if request.method == "POST":
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.save()
            return redirect('tarjeta_detail', pk=tarjeta.pk)
    else:
        form = TarjetaForm()
    return render(request, 'tarjetas/tarjeta_form.html', {'form': form})

def tarjeta_editar(request, pk):
    tarjeta = get_object_or_404(Tarjeta, pk=pk)
    if request.method == "POST":
        form = TarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.save()
            return redirect('tarjeta_detail', pk=tarjeta.pk)
    else:
        form = TarjetaForm(instance=tarjeta)
    return render(request, 'tarjetas/tarjeta_form.html', {'form': form})

def tablero_detail(request, pk):
    tablero = get_object_or_404(Tablero, pk=pk)
    return render(request, 'tableros/tablero_detail.html', {'tablero': tablero})

def tablero_nuevo(request):
    if request.method == "POST":
        form = TableroForm(request.POST)
        if form.is_valid():
            tablero = form.save(commit=False)
            tablero.save()
            return redirect('tablero_detail', pk=tablero.pk)
    else:
        form = TableroForm()
    return render(request, 'tableros/tablero_form.html', {'form': form})

