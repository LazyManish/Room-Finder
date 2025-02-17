from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('buyer','Buyer'),
        ('seller','Seller'),
    ]

    role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='buyer')


    def __str__(self):
        return f"{self.username}-({self.role})"


