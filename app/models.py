from django.db import models

# Create your models here.

class user_registration(models.Model):
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.username

class data_form(models.Model):
    name = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(null=True)
    age = models.CharField(max_length=240, null=True)
    gender = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=240, null=True)
    address = models.CharField(max_length=240, null=True)
    District = models.CharField(max_length=240, null=True)
    Branch = models.CharField(max_length=240, null=True)
    account = models.CharField(max_length=240, null=True)
    name = models.CharField(max_length=240, null=True)
    meterials = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.name