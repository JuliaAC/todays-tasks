from django.db import models
from django.utils import timezone


class Task(models.Model):
	author = models.ForeignKey('auth.User')
	task = models.CharField(max_length=200)
	list = models.ForeignKey('List')
	due_date = models.DateTimeField(
			default=timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.task

class List(models.Model):
	list = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User')

	def publish(self):
		self.save()

	def __str__(self):
		return self.list