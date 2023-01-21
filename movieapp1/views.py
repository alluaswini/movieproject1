from django.shortcuts import render,redirect
from movieapp1.models import movies
from .form import movieform


# Create your views here.
def addform(request):
    form=movieform()
    if request.method == "POST":
        form = movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/list')

    return render(request,'movieapp1/addform.html',{'form':form})

def addmovie(request):
    e=movies.objects.all()
    return render(request,'movieapp1/addlist.html',{'movie':e})

def home_view(request):
    return render(request,'movieapp1/home.html')
