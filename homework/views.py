from django.shortcuts import render
from homework.models import Page, Cities


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
    context = {'title':Cities, 'cities':all_cities}
    return render(request, 'cities.html', context)



# Create your views here.
