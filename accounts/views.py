# Create your views here.
from django.shortcuts import render,redirect
from content.models import Content
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
    # return render(request,'accounts/register.html')

def dashboard(request):
    content = Content.objects.all()
    return render(request,'dashboard.html',{'content':content})

def forgotPassword(request):
    return render(request,'forgotPassword.html')

def delete_content(request, id):
    contentone=Content.objects.get(pk=id).delete()
    return redirect("dashboard")