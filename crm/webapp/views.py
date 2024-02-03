from django.shortcuts import render, redirect

from . models import Record

from django.contrib import messages 

from .forms import createUserForm, LoginForm, CreateTaskForm, UpdateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'webapp/index.html')



def register(request):
    
    form =createUserForm()
    
    
    if request.method=='POST':
        form =createUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('my_login')


    context={'form':form}
    return render(request,'webapp/register.html', context=context)


def my_login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
                

    context={'form':form}
    return render(request, 'webapp/login.html', context=context)



def userLogOut(request):
    auth.logout(request)
    return redirect('my_login')


@login_required(login_url='my_login')
def dashboard(request):
    my_tasks=Record.objects.all()
    context={'my_tasks':my_tasks}

    return render(request, 'webapp/dashboard.html', context=context)


@login_required(login_url='my_login')
def create_task(request):
    form=CreateTaskForm()

    if request.method =='POST':
        form=CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully")
            return redirect('dashboard')

    context={'form':form}

    return render(request, 'webapp/create.html', context=context)


@login_required(login_url='my_login')
def update_task(request, pk):
    task=Record.objects.get(id=pk)

    form=UpdateTaskForm(instance=task)
    if request.method== 'POST':
        form=UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            
    context={'form':form}
    return render(request, 'webapp/edit.html', context)


@login_required(login_url='my_login')
def singleTask(request, pk):
    all_tasks=Record.objects.get(id=pk)
    context={'task':all_tasks}

    return render(request, 'webapp/view.html', context)


@login_required(login_url='my_login')
def delete_task(request, pk):
    task=Record.objects.get(id=pk)
    task.delete()
    messages.success(request, "Task Deleted successfully")
    
    return redirect('dashboard')
    