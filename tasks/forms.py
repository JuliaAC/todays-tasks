from django import forms

from .models import Task, List

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('list',)
		
class TaskForm(forms.ModelForm):
	
	class Meta:
		model = Task
		fields = ('task', 'list', 'due_date',)