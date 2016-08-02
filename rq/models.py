from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    q = models.TextField(max_length=100)
    a = models.TextField(blank=True)
    cdt = models.DateTimeField(null=True, auto_now_add=True)
    asker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_asker')
    assignee = models.ForeignKey(User, null=True, related_name='user_assignee')

    def __str__(self):
        return self.q


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)
