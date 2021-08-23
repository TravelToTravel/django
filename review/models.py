from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='review', null=True)

    subject = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='review/', blank=True)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
