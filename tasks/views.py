from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task, List
from .forms import TaskForm, ListForm

# Create your views here.
def task_list(request):
	tasks = Task.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
	if request.method == "POST":
		tform = TaskForm(request.POST)
		if tform.is_valid():
			task = form.save(commit=False)
			task.author = '-'
			task.save()
			return redirect('task_list')
	else:
		tform = TaskForm()
	return render(request, 'tasks/task_list.html', {'tasks' : tasks, 'tform' : tform},)
	
def add_list(request):
	if request.method == "POST":
		lform = ListForm(request.POST)
		if lform.is_valid():
			list = form.save(commit=False)
			list.author = '-'
			list.save()
			return redirect('task_list')
	else:
		lform = ListForm()
	return render(request, 'tasks/add_list.html', {'lform': lform})
