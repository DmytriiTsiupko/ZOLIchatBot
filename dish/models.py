from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    photo = models.ImageField(upload_to='dishes/', blank=True)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag} {self.name}"



