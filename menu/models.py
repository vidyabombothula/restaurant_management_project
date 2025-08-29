from django.db import models
from django.contrib.auth.models importUser

class Menu(models.Model):
    namr=models.CharField(max_length=100)
    price=models.DecimalFoeld(max_length=6,decimal_place=2)


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE=[
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ("COMPLETED",'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu)
    total_amount=models.DEcimalField(max_length=8,decimal_place=2)
    status=models.CharField(max_length20, choices=STATUS_CHOICE,default='PENDING')

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
