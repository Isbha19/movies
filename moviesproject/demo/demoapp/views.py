from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'home.html')
def result(request):
     a=int(request.GET['number1'])
     b=int(request.GET['number2'])
     add=a+b
     sub=a-b
     mul=a*b
     div=a/b
     return render(request,'result.html',{"addition":add,"subtraction":sub,"multiplication":mul,"division":div})






