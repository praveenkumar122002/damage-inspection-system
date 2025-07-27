from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass  # Use default Django fields (username, password)

class Inspection(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('completed', 'Completed'),
    ]

    vehicle_number = models.CharField(max_length=20)
    inspected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    damage_report = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
