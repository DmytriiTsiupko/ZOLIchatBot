# Generated by Django 4.2.1 on 2023-06-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0010_alter_dish_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
    ]
