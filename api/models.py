from django.db import models


class User(models.Model):
    mail = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=True)


class Profile(models.Model):
    name = models.CharField(max_length=20)
    profile = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Info(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

