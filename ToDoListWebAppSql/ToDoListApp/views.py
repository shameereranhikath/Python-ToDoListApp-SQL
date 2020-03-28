from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList
from django.utils import timezone
import threading

# Create your views here.


def index(request):
    timer = threading.Timer(5.0,index) 
    TodaData=ToDoList.objects.all()
    timer.start() 
    return render(request,'index.html',{'TodaData':TodaData})
    # return HttpResponse("haoooo")

def AddItem(request):
    currentdate=timezone.now()
    txtdata=request.POST["content"]
    ToDoList.objects.create(created_date=currentdate,text=txtdata)
    return HttpResponseRedirect("/ToDoList/")

def DeleteItem(request,todo_list):
     ToDoList.objects.get(id=todo_list).delete()
     return HttpResponseRedirect("/ToDoList/")

