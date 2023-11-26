from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=20)

class Time(models.Model):
  name = models.CharField(max_length=20)

class Price(models.Model):
  PRICE_CATEGORY = [
    ("G", "Gratuito"),
    ("1", "R$10-R$20"),
    ("2", "R$20-R$40"),
    ("3", "R$40-"),
  ]
  price = models.CharField(max_length=1, choices = PRICE_CATEGORY, null=True)

class Events(models.Model):
  
  name = models.CharField(max_length=200)
  link = models.URLField(max_length=200, blank=True)
  price = models.ManyToManyField(Price)
  date = models.DateTimeField(null=True)
  time = models.ManyToManyField(Time)
  category = models.ManyToManyField(Category)
  location = models.CharField(max_length=200)
  
  

  
