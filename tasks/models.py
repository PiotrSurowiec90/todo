from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    text = models.CharField(max_length = 200)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.text