from django.db import models
from django.contrib import staticfiles
import os

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='assets/')

    def filename(self):
        return self.image.split("/")[1]
