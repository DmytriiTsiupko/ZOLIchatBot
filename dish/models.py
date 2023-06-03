from django.db import models


class Dish(models.Model):
    DIET_CHOICES = (
        ('non-vegetarian', 'Non-Vegetarian'),
        ('vegetarian', 'Vegetarian'),
    )
    SPICY_CHOICES = (
        ('mild', 'Mild'),
        ('medium', 'Medium'),
        ('spicy', 'Spicy'),
    )
    TAG_CHOICES = [
        ('Pizza Rosse', 'Pizza Rosse'),
        ('Pizza Bianche', 'Pizza Bianche'),
        ('Makaron', 'Makaron'),
        ('Przystawki', 'Przystawki'),
        ('Cafeteria', 'Cafeteria'),
        ('Bevande', 'Bevande'),
        ('Alcohol', 'Alcohol'),
        ('Gnocchi ziemniaczane', 'Gnocchi ziemniaczane'),
        ('Gnocchi serowe', 'Gnocchi serowe'),
        ('Ravioli', 'Ravioli'),
        ('Lasagne', 'Lasagne'),
        ('Sałatki', 'Sałatki'),
        ('Zupy', 'Zupy')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_vegan = models.CharField(max_length=20, choices=DIET_CHOICES, default='non-vegetarian')
    spiciness = models.CharField(max_length=20, choices=SPICY_CHOICES, default='mild')
    photo = models.ImageField(upload_to='media/', blank=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.tag} {self.name}"


