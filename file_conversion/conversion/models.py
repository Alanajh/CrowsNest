from django.db import models

class User(models.Model):
  username = models.CharField(max_length=55)
  password = models.CharField(max_length=55)
  type = models.CharField(max_length=25)
  
class Transform(models.Model):
  file = models.FileField()
  columns = models.CharField(max_length=10)
  rows = models.CharField(max_length=10)
  
class Results(models.Model):
  table = models.TextField()