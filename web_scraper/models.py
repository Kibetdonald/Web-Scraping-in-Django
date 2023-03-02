from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
