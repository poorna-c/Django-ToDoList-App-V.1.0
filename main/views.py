from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList
from django.contrib import messages
import datetime
# Create your views here.
def index(request):
    items = ToDoList.objects.all()
    return render(request, 'index.html',{'items':items,'today':datetime.date.today})


def update(request):
    items = ToDoList.objects.all()
    if request.method== 'POST':
        print(request.POST)
        if request.POST.get('add'):
            t = ToDoList()
            t.text = request.POST['text']
            if t.text == "":
                return redirect('/')
            else:
                t.save()
        
        if request.POST.get('save'):
            for item in items:
                if request.POST.get("C" + str(item.id)) == "clicked":
                    item.complete = True
                    item.completed_date = datetime.datetime.now()
                else:
                    item.complete = False
                    item.completed_date = None
                item.text = request.POST.get('data'+ str(item.id))
                item.save()
            
        if request.POST.get('delete'):
            ToDoList.objects.filter(id=request.POST.get('delete')).delete()

        return redirect('/')
