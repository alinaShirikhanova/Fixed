from django.db import models
from users.models import Usery

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="category_images", null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.description}'



class Basket(models.Model):
    user = models.ForeignKey(to=Usery, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)


    def __str__(self):
        return f'корзина пользователя {self.user.name}, товар: {self.product.name}'







