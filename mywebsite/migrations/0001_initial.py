# Generated by Django 2.1a1 on 2018-07-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(help_text='Enter the menu item name', max_length=50, verbose_name='Menu Item name')),
                ('menucategory', models.CharField(choices=[('veg', 'Vegetarian'), ('non-veg', 'Non Vegetarian')], default='veg', help_text='Describe if the dish is veg or non-veg', max_length=7, verbose_name='Select the dish type')),
                ('items_in_stock', models.IntegerField(default=0, help_text='Enter the number of items in stock', verbose_name='Number of items in stock')),
                ('price', models.FloatField(default=0.0, help_text='Enter the price of the menu item', verbose_name='Price of the menu item')),
            ],
            options={
                'ordering': ['recipe_name'],
            },
        ),
    ]