from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Queries(models.Model):
    destination = models.CharField(max_length= 20)
    departure = models.CharField(max_length= 20)
    date_of_travel = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.name} - {self.destination}"