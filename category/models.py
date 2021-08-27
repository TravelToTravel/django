from django.db import models

# Create your models here.


class Party(models.Model):
    headcount = models.CharField(max_length=20)

    def __str__(self):
        return self.headcount


class Age(models.Model):
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.age


class Location(models.Model):
    area = models.CharField(max_length=20)

    def __str__(self):
        return self.area


class Purpose(models.Model):
    purpose = models.CharField(max_length=20)

    def __str__(self):
        return self.purpose
