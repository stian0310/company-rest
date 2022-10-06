from django.db import models
from django.core.validators import RegexValidator

class Enterprise(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    nit = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$', message='Phone number must be entered in the format +57123456789') 
    phone = models.CharField(max_length=17, validators=[phone_regex])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
