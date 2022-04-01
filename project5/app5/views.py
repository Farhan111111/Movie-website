from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app5.models import Movie
from .forms import Movie_form


def fun1(request):
    value = Movie.objects.all()
    return render(request, 'index.html', {'key': value})


def fun2(request, movie_list):
    movie = Movie.objects.get(id=movie_list)
    return render(request, 'details.html', {'kiy': movie})


def add_movie(request):
    form = Movie_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'add.html', {'form': form})


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movie_form(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
