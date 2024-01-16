from django.db import models

# Create your models here.


class Member (models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)

    # One way of presenting reader-friendly string in admin is
    # by defining a string function like this one:
    # def __str__(self):
    #    return f"{self.firstname, self.lastname}"
