from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    is_spam = models.BooleanField(default=False)
    is_registered  = models.BooleanField(default=False)
    contact_of = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, default=None)

    def mark_as_registered(self):
        self.is_registered = True
        self.save()

    def mark_as_spam(self):
        self.is_spam = True
        self.save()