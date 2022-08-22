from django.db import models

class Accounts(models.Model):
    nickname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)