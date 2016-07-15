from celery import task
from django.contrib.auth.models import User
import random

@task()
def hello():
	print("Hello world")

@task()
def assignQuestion(question):
	count = User.objects.all().count()
	assigned = False
	while not assigned:
		try:
			user = User.objects.get(pk=random.randint(1, count))
			if user.id == question.asker.id:
				continue
			question.assignee = user
			question.save()
			print("Question reassigned" + str(question.id))
			break
		except:
			continue