from django.shortcuts import render
from gallary.models import Gallary

def home(request):
    gallarys=Gallary.objects
    return render(request,'home.html',{'gallarys':gallarys})