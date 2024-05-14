from django.db import models

class User(models.Model):
  username = models.CharField(max_length=55)
  password = models.CharField(max_length=55)
  type = models.CharField(max_length=25)