from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.IntegerField()
    country = models.CharField(max_length=30)


class Cars(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=40)
    type_cars = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    power = models.IntegerField()


class StatusDrivers(models.Model):
    name = models.CharField(max_length=20)


class Drivers(models.Model):
    name = models.CharField(max_length=40)
    number = models.IntegerField()
    email = models.EmailField()
    status_code = models.ForeignKey(StatusDrivers, null=True, on_delete=models.SET_NULL)


class LogCars(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    date = models.DateTimeField()
