from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=123)
    text = models.TextField(max_length=100000)

    def __str__(self):
        return self.title


