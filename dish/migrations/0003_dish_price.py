# Generated by Django 4.2.1 on 2023-05-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_alter_dish_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
