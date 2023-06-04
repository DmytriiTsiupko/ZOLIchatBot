# Generated by Django 4.2.1 on 2023-06-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0003_dish_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='dish',
            name='tag',
            field=models.CharField(choices=[('Pizze Rosse', 'Pizze Rosse'), ('Pizze Bianche', 'Pizze Bianche'), ('Makaron', 'Makaron'), ('Czarny Makaron', 'Czarny Makaron'), ('Przystawki', 'Przystawki'), ('Cafeteria', 'Cafeteria'), ('Bevande', 'Bevande'), ('Alcohol', 'Alcohol'), ('Gnocchi', 'Gnocchi'), ('Ravioli', 'Ravioli'), ('Lasagne', 'Lasagne'), ('Sałatki', 'Sałatki')], max_length=50),
        ),
    ]