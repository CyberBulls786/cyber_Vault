from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item



def main(request):
    return render(request, 'main.html')

def blogs(request):
    return render(request, 'blogs.html')

def contactus(request):
    return render(request, 'contactus.html')


def index(request):
    return render(request, 'index.html')



# Create your views here.

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
        else:
            user= User.objects.create_user(username=username,password=password)
            user.save()
            messages.success(request,'accout created successfully')
            return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    items= Item.objects.all()
    return render(request,'home.html', {'items' : items})

def todo_list(request):
    todos = Item.objects.order_by('-id')
    return render(request , 'cybervault.html' , {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        username_vault = request.POST.get('username_vault')
        pass_vault = request.POST.get('pass_vault')
        Item.objects.create(platform = platform , username_vault = username_vault , pass_vault= pass_vault)
    return redirect('todo_list')

def delete_todo(request,todo_id):
    todo = Item.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

