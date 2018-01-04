from __future__ import unicode_literals
from django.contrib.auth.models import User
from datetime import datetime

from django.db import models

class Task(models.Model):
    task_id = models.CharField(max_length=10)
    task_name = models.CharField(max_length=250)

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    is_done = models.BooleanField(choices=BOOL_CHOICES)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    done_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.task_name