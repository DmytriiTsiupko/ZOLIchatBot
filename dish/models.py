from django.db import models


class Dish(models.Model):
    TAG_CHOICES = [
        ('Pizze Rosse', 'Pizze Rosse'),
        ('Pizze Bianche', 'Pizze Bianche'),
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
    photo = models.ImageField(upload_to='media/', blank=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.tag} {self.name}"


