from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Account(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    number = models.DecimalField(max_digits=10, decimal_places=0, unique=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    
    def __str__(self):
        return f"{self.user} has ${self.amount}"

class Spending(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=100, null=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} spent ${self.item_price} on {self.item}"

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"

class Transfer(models.Model):
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name="money_sender")
    recipient = models.ForeignKey("User", on_delete=models.PROTECT, related_name="money_reciever")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    received = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.sender} sent ${self.amount} to {self.recipient}"

class Budget(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=False)
    item = models.CharField(max_length=100, null=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} spent ${self.item_price} on {self.item}"

class User_budget(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.user} add ${self.amount} in {self.category} on {self.timestamp}"