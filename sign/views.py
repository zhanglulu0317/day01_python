from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from numpy.distutils.fcompiler import none


def index(request):
    return render(request,'index.html')


def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')

        if username=='admin'and password=='admin123':
           response = HttpResponse()
           response=HttpResponseRedirect('/event_manage')
           request.session['user']=username
           return response
        else:
           return render(request,'index.html',{'error':'username or password error'})

def event_manage(request):
          username=request.session.get('user','')
          return render(request,"event_manage.html",{'user':username})