from typing import Sized
from django.db import models
from django import db
from django.db.models.aggregates import Max
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table='menu'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    class Meta:
        db_table='categories'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)
    class Meta:
        db_table='nutritions'

class Product(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    nutritions = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category,  on_delete=models.CASCADE)
    
    class Meta:
        db_table='products'

class Image(models.Model):
    image_url = models.CharField(max_length=200)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table='images'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table='allergy'

class Allergy_product(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table='allergy_products'