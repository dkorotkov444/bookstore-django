# sales/admin.py
# This file registers the Sale model with the Django admin site.
from django.contrib import admin
from .models import Sale

# Register your models here.
admin.site.register(Sale)
