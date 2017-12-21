from django.contrib import admin
from .models import List
from .models import Task

admin.site.register(List)
admin.site.register(Task)