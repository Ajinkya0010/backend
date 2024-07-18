from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    emergencyContact = models.CharField(max_length=100)
    caretakerId = models.CharField(max_length=50, default='') 
    pincode = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
