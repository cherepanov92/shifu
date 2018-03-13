from django.shortcuts import render
# from django.template import RequestContext, loader


# def index(request):
#     return HttpResponse("You're looking at question")

def index(request):
    my_list = ['one', 'two', 'end']
    context = {'question_list': my_list}
    return render(request, 'index.html', context)


# Create your views here.
