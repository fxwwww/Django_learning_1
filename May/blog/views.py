from django.shortcuts import render
from .models import Student
# Create your views here.
# from django.http import HttpResponse



def NewUser(request):
    studentname=request.POST.get('postname')
    studentid=request.POST.get('postid')
    s = Student()
    s.studentid=studentname
    s.studentid=studentid
    s.save()
    return render(request,'NewUser.html', locals())

def index(request):
    namelist = Student.objects.all()
    return render(request,'index.html', locals())

    #return HttpResponse("index.html")

