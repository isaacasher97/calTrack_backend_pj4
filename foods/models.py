from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)