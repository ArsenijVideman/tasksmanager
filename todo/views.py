from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


class Feature:
    def index(request):
        tasks = Task.objects.order_by('-id')
        title = 'Home Page'
        return render(request, 'index.html', {'title': title.capitalize(), 'tasks': tasks})

    def about_me(request):
        return render(request, 'about_me.html')

    def resume(request):
        return render(request, 'resume.html')

    def create_new_task(request):
        error = ''
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                error = 'Something went wrong'

        form = TaskForm()
        context = {
            'form': form,
            'error': error,
        }
        return render(request, 'create.html', context)
