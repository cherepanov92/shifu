from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("You're looking at question")

def test(request ,text = 'не найден'):
    return HttpResponse('Твой текст {}'.format(text))

# Create your views here.
