from django.shortcuts import render
from django.utils import timezone
from .models import Task, List

# Create your views here.
def task_list(request):
	tasks = Task.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
	return render(request, 'tasks/task_list.html', {'tasks' : tasks})