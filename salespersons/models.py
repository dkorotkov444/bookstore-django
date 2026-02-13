# salespersons/models.py
# This file defines the Salesperson model for the bookstore application.
from django.db import models
from django.contrib.auth.models import User

# Salesperson model
class Salesperson(models.Model):
    # Django built-in User record is linked to the Salesperson model using this OneToOneField.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)
    bio = models.TextField(default='no bio...', blank=True, null=False)

    def __str__(self):
        return f"{self.user.username}"