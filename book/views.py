from django.shortcuts import render,redirect
from django.http import HttpResponse
from book.models import *

# Create your views here.
def registration(request):
    return render(request,'registration.html')
def register(request):
    u=booker()
    u.name=request.GET['name']
    u.phno=request.GET['phno']
    u.email=request.GET['email']
    u.pwd=request.GET['pwd']
    u.adh=request.GET['adh']
    u.add=request.GET['add']
    u.save()
    return redirect('../registration')
def index(request):
    return render(request,'index.html')
def login (request):
    return render(request,'login.html')
def log(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if len(a) and len(b) and booker.objects.filter(adh=a,pwd=b):
        return redirect('../index')
    else:
        return render(request,'login.html')
def book(request):
    u=room.objects.all()
    return render(request,'book.html',{'u':u})
def admin(request):
    return render(request,'admin.html')
def adregister(request):
    u=room()
    u.no=request.GET['no']
    u.capacity=request.GET['cap']
    u.save()
    return render(request,'admin.html')
def booking(request,id):
    u=room.objects.get(id=id)
    u.startdate=request.GET['stdate']
    u.enddate=request.GET['eddate']
    u.name=request.GET['gn']
    u.save()
    return render(request,'confirm.html',{'u':u})
def bookedroom(request):
    u=room.objects.all()
    return render(request,'bookedroom.html',{'u':u})
def insert(request):
    return render(request,'insert.html')
def ins(request):
    u=room()
    u.name=request.GET['a1']
    u.no=request.GET['a2']
    u.capacity=request.GET['a3']
    u.startdate=request.GET['a4']
    u.enddate=request.GET['a5']
    u.save()
    return render(request,'insert.html')