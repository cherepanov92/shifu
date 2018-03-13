from django.shortcuts import render, redirect
from homework.models import Page, Cities
from .forms import CityForm


# def index(request):
#     return HttpResponse("You're looking at question")

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


