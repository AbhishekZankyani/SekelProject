from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class Lead(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=20)
    Products = models.ManyToManyField(Product)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
