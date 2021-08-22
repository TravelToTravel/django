from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Festival(models.Model):
    image = models.ImageField(upload_to='festival/', null=False)
    title = models.CharField(max_length=50, null=False)
    duration = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title
