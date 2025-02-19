from django.db import models
from django.core.validators import MinValueValidator
from User.models import CustomUser

# Create your models here.


class Room(models.Model):

    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='room_images/', null=False, blank=False)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField( max_length=12, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.admin} rooms"
    


