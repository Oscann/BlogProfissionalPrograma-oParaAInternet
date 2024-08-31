from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=150)
    expertise = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    coordination = models.CharField(max_length=30)
    certificate = models.ImageField(upload_to="certificates/")

class Project(models.Model):
    name = models.CharField(max_length=100)
    coordination = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

class Technology(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='techs/')