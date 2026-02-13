# salespersons/admin.py
# This file registers the Salesperson model with the Django admin site.
from django.contrib import admin
from .models import Salesperson

# Register your models here.
admin.site.register(Salesperson)
