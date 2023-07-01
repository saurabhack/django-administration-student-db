from django.shortcuts import render
from django.http import HttpResponse
from .models import paste
# Create your views here.
def index(request):
    yess=paste.objects.all()
    return render(request,'index.html',{'yess':yess})
    #at=info.objects.all()

#{'adds':adds}

def profile(request):
    text2=request.POST['text2']
    text3=request.POST['text3']
    return render(request,'profile.html' ,{'text2':text2 ,'text3':text3})


