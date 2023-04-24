from django.shortcuts import render

from .models import Company, Cars, LogCars, Drivers, StatusDrivers
from .forms import *


def createCar(request):
    if request.method == "POST":
        name = request.POST.get("name")
        power = request.POST.get("power")
        type_cars = request.POST.get("type_cars")
        color = request.POST.get("color")
        company = request.POST.get("company")
        id_company = Company.objects.filter(id = company).get()
        car = Cars.objects.create(name=name, power=power, type_cars=type_cars, color=color, company=id_company)
        car.save()
        carform = CarForm()
        return render(request, "createCar.html", {"form": carform})
    else:
        carform = CarForm()
        return render(request, "createCar.html", {"form": carform})


def createStatus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        status = StatusDrivers.objects.create(name=name)
        status.save()
        statusForm = StatusForm()
        return render(request, "createStatus.html", {"form": statusForm})
    else:
        statusForm = StatusForm()
        return render(request, "createStatus.html", {"form": statusForm})


def createCompany(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        country = request.POST.get("country")
        company = Company.objects.create(name=name, email=email, number=number, country=country)
        company.save()
        companyform = CompanyForm()
        return render(request, "createCompany.html", {"form": companyform})
    else:
        companyform = CompanyForm()
        return render(request, "createCompany.html", {"form": companyform})


def createDrivers(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        status_code = request.POST.get("status")
        id_status = StatusDrivers.objects.filter(id=status_code).get()
        driver = Drivers.objects.create(name=name, email=email, number=number, status_code=id_status)
        driver.save()
        driversform = DriversForm()
        return render(request, "createDrivers.html", {"form": driversform})
    else:
        driversform = DriversForm()
        return render(request, "createDrivers.html", {"form": driversform})


def viewCompany(request):
    companies = Company.objects.all()
    return render(request, "viewCompany.html", {"DB": companies})


def viewCars(request):
    cars = Cars.objects.all()
    return render(request, "viewCars.html", {"DB": cars})


def viewDrivers(request):
    drivers = Drivers.objects.all()
    return render(request, "viewDrivers.html", {"DB": drivers})