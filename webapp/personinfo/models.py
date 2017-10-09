from django.db import models

class Household(models.Model):
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=10)
    bedrooms = models.IntegerField()

    def __str__(self):
        return self.city

class Person(models.Model):
    household = models.ForeignKey(Household, on_delete = models.CASCADE, null=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)

    def __str__(self):
        return self.first_name


class Vehicle(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=50)
    model_name = models.CharField(max_length = 20)
    year = models.IntegerField()
    liceance_plate = models.CharField(max_length= 20,)

    def __str__(self):
        return self.model_name
