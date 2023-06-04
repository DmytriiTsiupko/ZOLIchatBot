# Generated by Django 4.2.1 on 2023-06-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0012_alter_dish_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='is_vegan',
            field=models.CharField(choices=[('non-vegetarian', 'Non-Vegetarian'), ('vegetarian', 'Vegetarian')], default='non-vegetarian', max_length=20),
        ),
        migrations.AlterField(
            model_name='dish',
            name='tag',
            field=models.CharField(choices=[('pizza Rosse', 'Pizza Rosse'), ('pizza Bianche', 'Pizza Bianche'), ('pasta', 'Pasta'), ('starters', 'Starters'), ('cafeteria', 'Cafeteria'), ('drinks', 'Drinks'), ('alcohol', 'Alcohol'), ('gnocchi (potato)', 'Gnocchi (potato)'), ('gnocchi (cheese)', 'Gnocchi (cheese)'), ('ravioli', 'Ravioli'), ('lasagne', 'Lasagne'), ('salads', 'Salads'), ('soup', 'Soup')], max_length=50),
        ),
    ]
