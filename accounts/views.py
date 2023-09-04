# Create your views here.
from django.shortcuts import render,redirect
from content.models import Content
from content.forms import ContentForm
from .forms import RegisterForm
from django.contrib.auth import login,logout,authenticate

def login_user(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=user_name,password=password)
        login(request,user)
        return redirect('dashboard')
    return render(request,'login.html')

def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect('dashboard')
    return render(request,'register.html',{'form':form})
    # return render(request,'accounts/register.html')


def signout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    content = Content.objects.all()
    return render(request,'dashboard.html',{'content':content})

def forgotPassword(request):
    return render(request,'forgotPassword.html')

def delete_content(request, id):
    contentone=Content.objects.get(pk=id).delete()
    return redirect("dashboard")

def addItem(request):
    form = ContentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'add_item.html',context )
   
def edit_item(request, id):
    name = Content.objects.get(pk = id)
    form = ContentForm(instance = name)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance = name)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'add_item.html', context)