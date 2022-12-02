from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from .models import Movies


# Create your views here.
def test(request):
    movies=Movies.objects.all()
    context={
        'Table':movies
    }
    return render(request,"index.html",context)
def detail(request,movieid):
    movie=Movies.objects.get(id=movieid)
    return render(request,"details.html",{"res":movie})
def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        image=request.FILES['image']
        movies=Movies(name=name,desc=desc,year=year,image=image)
        movies.save();
        return redirect('/')
    return render(request,"add.html")

def update(request,id):
    model=Movies.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=model)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'movieid':model})
def delete(request,id):
    if request.method=='POST':
        model = Movies.objects.get(id=id)
        model.delete()
        return redirect('/')
    return render(request,"delete.html")

