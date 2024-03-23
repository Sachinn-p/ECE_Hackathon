from django.db import models
from django.contrib.auth.models import AbstractUser
#from .models import UserDetails


class User(AbstractUser):
    phone = models.CharField(max_length=13)
    # Add related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField('auth.Group', related_name='myapp_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='myapp_users')



class UserDetails(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    phone = models.CharField(max_length=13)

class LoanRequest(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()

class UserPurpose(models.Model):
    BORROWER = 'borrower'
    LENDER = 'lender'
    ROLE_CHOICES = [
        (BORROWER, 'Borrower'),
        (LENDER, 'Lender'),
    ]
    
    user = models.CharField(max_length=60,default="")
    password = models.CharField(max_length=13)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class LoanRequest(models.Model):
    amount = models.FloatField()
    description = models.TextField()
