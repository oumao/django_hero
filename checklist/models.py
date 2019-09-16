from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return "<Name: {}>".format(self.name)
