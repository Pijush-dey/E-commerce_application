from django.db import models

# Create your models here.
class CustomerInfo(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=100)

    class Meta:                               #Change model class name in Django admin interface
        verbose_name="Customer's Info"
        verbose_name_plural="Customer's Info"