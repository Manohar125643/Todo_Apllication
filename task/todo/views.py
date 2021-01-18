from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo




def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/index.html',context)


def insert(request: HttpRequest):
    todo = Todo(content=request.POST['name'])
    todo.save()
    return render(request, 'todos/index.html')

def delete(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/')