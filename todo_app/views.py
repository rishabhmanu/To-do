from django.shortcuts import render

def home(request):
    return render(request, 'todo_app/home.html', {})
