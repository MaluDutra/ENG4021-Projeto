from django.db import models
# from django.contrib.auth.models import User
# from django.db.models import Avg


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
  
  RECOMENDATION_CATEGORY = [
    ("1", "1 estrela"),
    ("2", "2 estrela"),
    ("3", "3 estrela"),
    ("4", "4 estrela"),
    ("5", "5 estrela")
  ]
  name = models.CharField(max_length=200)
  link = models.URLField(max_length=200, blank=True)
  price = models.ManyToManyField(Price)
  date = models.DateTimeField(null=True)
  time = models.ManyToManyField(Time)
  category = models.ManyToManyField(Category)
  location = models.CharField(max_length=200)
  recomendation = models.CharField(max_length=1, choices = RECOMENDATION_CATEGORY, null=True)

#   def average_rating(self) -> float:
#     return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

#   def __str__(self):
#     return f"{self.header}: {self.average_rating()}"
  

# class Rating(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   post = models.ForeignKey(Events, on_delete=models.CASCADE)
#   rating = models.IntegerField(default=0)

#   def __str__(self):
#     return f"{self.post.header}: {self.rating}"