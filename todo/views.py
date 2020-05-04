from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.
def index(request):

    #to fetch all results in Todo
    # this will return cursor, similar to db['collection'].find()
    all_todos = Todo.objects.all() 

    return render(request, 'todo/index.template.html', {
        'all_todos':all_todos
    })

