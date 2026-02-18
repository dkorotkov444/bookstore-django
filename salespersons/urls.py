from django.urls import path
from .views import salesperson

urlpatterns = [
    path('', salesperson, name='salesperson-home'),
]
