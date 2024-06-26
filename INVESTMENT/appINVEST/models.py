from django.db import models
from django.contrib.auth.models import AbstractUser, User



    
class Asset(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    investor = models.ForeignKey(User, on_delete = models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    
    def total_value(self):
        return self.asset.price * self.quantity
    
    def __str__(self):
        return f"{self.investor.username}'s portfolio -' {self.asset.name}"
    
    
    
# class User(AbstractUser):
#     pass

# class Asset(models.Model):
#     name=models.CharField(max_length=100)
#     ticker=models.CharField(max_length=10)
#     quanity=models.IntegerField(default=0)
#     price=models.DecimalField()

# class Portfolio(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     assets=models.ManyToManyField(Asset)
# class User(AbstractUser):
#     pass