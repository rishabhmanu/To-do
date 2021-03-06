from django.shortcuts import render, redirect
# from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ToDoForm
from .models import Todo

@login_required
def home(request):
    tasks = Todo.objects.filter(author=request.user)
    return render(request, 'todo_app/home.html', {'tasks':tasks})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'todo_app/signup.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.status = form.cleaned_data.get('status')
            todo.save()
            return redirect('home')
    else:
        form = ToDoForm()
    return render(request, 'todo_app/todo_new.html', {'form': form})
