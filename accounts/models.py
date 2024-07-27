from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    role = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    username = None
    email = models.EmailField(unique=True)
    full_names = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=20, choices=role, default='Member')
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_names', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.full_names
    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dp = models.ImageField(default='coding.jpeg', upload_to='profile_pics')
    club_role = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.user.email