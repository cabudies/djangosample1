from django.db import models
from django.urls import reverse


class Menu(models.Model):
    MENU_CATEGORY = (
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non Vegetarian'),
    )

    recipe_name = models.CharField(max_length=50, help_text='Enter the menu item name',
                                   verbose_name='Menu Item name')

    menucategory = models.CharField(max_length=7, choices=MENU_CATEGORY, default='veg',
                                    help_text='Describe if the dish is veg or non-veg',
                                    verbose_name='Select the dish type')

    items_in_stock = models.IntegerField(default=0, help_text='Enter the number of items in stock',
                                         verbose_name='Number of items in stock')

    price = models.FloatField(default=0.0, help_text='Enter the price of the menu item',
                              verbose_name='Price of the menu item')

    # models.CharField tells the type of field will be created in the database.
    # help_text defines the help text while entering the data into the database from the admin module.
    # verbose_name defines the human readable text for the database field while entering data into the database.
    # default defines the default value for the field.
    # null if true, django will store blank values as NULL.
    # blank if true, the field is allowed to be blank in your forms.
    # choices a group of choices for this field. You will get a select box with choices instead of the standard text field.
    # primary_key if true, sets the current field as the primary key for the model.
    # CharField, TextField (large strings), IntegerField, DateField and DateTimeField (auto_now = True), EmailField,
    # FileField, ImageField (used to upload files and images respectively, parameters, how and where to store the uploaded files.
    # AutoField (Autoincrement integer field)
    # ForeignKey is used to specify a one to many relationship to another database model
    # ManyToManyField is used to specify a many-to-many relationship

    # Use __str__ to return a human-readable string for each object.
    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    #  Meta
    class Meta:
        ordering = ["recipe_name"]
        # "-recipe_name" tells that the recipe name field should be come in reverse order.
        # e.g. ["recipe_name", "-price"] would sort recipe_name in ascending and then price in descending

    #################################################
    # Searching for record - ##

    # RecipeDetails.objects.all() - retreives all the objects
    # RecipeDetails.objects.filter(recipe_name__contains='hi')
    # RecipeDetails.objects.filter(recipe_name__contains='hi').count()
    # field lookup reference - https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups
    # Making queries - https://docs.djangoproject.com/en/2.0/topics/db/queries/

class CustomerOrder(models.Model):
    pass
