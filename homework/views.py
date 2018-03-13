from django.shortcuts import render, redirect
from homework.models import Page, Cities
from .forms import CityForm

def index(request):
    my_list = Page.objects.all()
    context = {'title':'index' ,'question_list': my_list}
    return render(request, 'index.html', context)

def page(request, title):
    db_page = Page.objects.get(title = title)
    context = {'title': db_page}
    return render(request, 'page.html', context)

def cities(request):
    all_cities = Cities.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # cities = form.save(commit=False)  #Если нужно изменить данные перед сохранением
            cities = form.save()
            cities.save()
            return redirect('cities')
    else:
        form = CityForm()
    context = {'title':Cities, 'cities':all_cities, 'form':form}
    return render(request, 'cities.html', context)

def new_city(request):
    all_cities = Cities.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # cities = form.save(commit=False)  #Если нужно изменить данные перед сохранением
            cities = form.save()
            cities.save()
            return redirect('cities')
    else:
        form = CityForm()
    context = {'title':Cities, 'cities':all_cities, 'form':form}
    return render(request, 'new_city.html', context)

def edit_city(request, id):
    all_cities = Cities.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # cities = form.save(commit=False)  #Если нужно изменить данные перед сохранением
            cities = form.save(commit=False)
            cities.id = id
            cities.save()
            return redirect('cities')
    else:
        form = CityForm()

    db_city = Cities.objects.get(id=id)
    context = {'title':Cities, 'cities':all_cities, 'form':form, 'text':db_city.name}
    return render(request, 'edit_city.html', context)

def del_city(request, id):
    Cities.objects.get(id = id).delete()
    return redirect('cities')

