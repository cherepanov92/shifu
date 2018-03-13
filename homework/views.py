from django.shortcuts import render
# from django.template import RequestContext, loader


# def index(request):
#     return HttpResponse("You're looking at question")

def index(request):
    my_list = ['one', 'two', 'end']
    context = {'title':'index' ,'question_list': my_list}
    return render(request, 'index.html', context)

def one(request):
    context = {'title': 'one'}
    return render(request, 'lesson2.html', context)

def two(request):
    context = {'title': 'two'}
    return render(request, 'lesson2.html', context)

def end(request):
    context = {'title': 'end'}
    return render(request, 'lesson2.html', context)


# Create your views here.
