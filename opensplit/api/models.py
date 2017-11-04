from django.contrib.auth import models
from django.db.models import Model, CharField, DateTimeField, ManyToManyField


class User(models.User):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Group(Model):
    groupname = CharField(max_length=100, primary_key=True)
    members = ManyToManyField(User)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

