from django.db import models


class Dish(models.Model):
    TAG_CHOICES = [
        ('Pizza', 'Pizza'),
        ('Makaron', 'Makaron'),
        ('Czarny Makaron', 'Czarny Makaron'),
        ('Przystawki', 'Przystawki'),
        ('Cafeteria', 'Cafeteria'),
        ('Bevande', 'Bevande'),
        ('Alcohol', 'Alcohol'),
        ('Gnocchi', 'Gnocchi'),
        ('Ravioli', 'Ravioli'),
        ('Lasagne', 'Lasagne'),
        ('Sałatki', 'Sałatki'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    photo = models.ImageField(upload_to='dishes/', blank=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)

    def __str__(self):
        return f"{self.tag} {self.name}"



