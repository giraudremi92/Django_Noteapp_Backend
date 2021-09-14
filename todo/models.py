from django.db import models

class Todo(models.Model):

    title = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    coordx = models.CharField(max_length=255, blank=True)
    coordy = models.CharField(max_length=255, blank=True)



