# Generated by Django 4.2.1 on 2023-06-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0011_alter_dish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='tag',
            field=models.CharField(choices=[('Pizza Rosse', 'Pizza Rosse'), ('Pizza Bianche', 'Pizza Bianche'), ('Makaron', 'Makaron'), ('Przystawki', 'Przystawki'), ('Cafeteria', 'Cafeteria'), ('Bevande', 'Bevande'), ('Alcohol', 'Alcohol'), ('Gnocchi ziemniaczane', 'Gnocchi ziemniaczane'), ('Gnocchi serowe', 'Gnocchi serowe'), ('Ravioli', 'Ravioli'), ('Lasagne', 'Lasagne'), ('Sałatki', 'Sałatki'), ('Zupy', 'Zupy')], max_length=50),
        ),
    ]