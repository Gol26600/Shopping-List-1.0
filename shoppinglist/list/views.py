from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home_view(request):
    items = Product.objects.all()
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'items': items,
               'form': form}
    return render(request, 'home.html', context)


def edit_product_view(request, pk):
    item = Product.objects.get(id=pk)
    form = ProductForm(instance=item)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'item': item,
               'form': form}
    return render(request, 'edit_product.html', context)


def delete_product_view(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'delete_product.html', context)


def products_view(request):
    items = Product.objects.all().order_by('name')
    context = {'items': items}
    return render(request, 'products.html', context)


def notes_view(request):
    item = Notes.objects.get(id=1)
    form = NotesForm(instance=item)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=item)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'item': item,
               'form': form}
    return render(request, 'notes.html', context)
