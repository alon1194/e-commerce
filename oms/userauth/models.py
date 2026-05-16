from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Custumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    Image = models.ImageField( upload_to='profile_image/',null = True, blank = True)
    phone_number = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return f"{self.user.username}'s Account"





