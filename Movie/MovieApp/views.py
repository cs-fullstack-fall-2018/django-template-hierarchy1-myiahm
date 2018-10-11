from django.shortcuts import render
from .models import MovieChoice


def index(request):
    latest_choice = MovieChoice.objects.all()
    context = {'latest_choice': latest_choice}
    return render(request, 'MovieApp/index.html', context)

def about(request):
    return render(request, 'MovieApp/about.html')

def test(request):
    return render(request, 'MovieApp/test.html')

def index2(request):
    latest_choice = MovieChoice.objects.all()
    context = {'latest_choice': latest_choice}
    return render(request, 'MovieApp/newIndex.html', context)
