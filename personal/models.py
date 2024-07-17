from django.db import models

# Create your models here.


class Me(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )

    name = models.CharField(max_length=200, null=True)
    born = models.DateField(null=True)
    age = models.FloatField(null=True)
    Phone = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    born = models.DateField(null=True)
    Bio = models.TextField(max_length=1000, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200, null=True)
    descript = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    image = models.ImageField('image/', null=True)
    descriptions = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
