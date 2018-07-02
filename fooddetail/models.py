from django.db import models
from django.utils import timezone


class Food(models.Model):

   food_text = models.CharField(max_length=200)
   number_sugar = models.IntegerField(default=0)
   
   def __str__(self):
      return self.food_text


