from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USZipCodeField
from localflavor.us.us_states import STATE_CHOICES


class Address(models.Model):
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.ChoiceField(choices=STATE_CHOICES)
    zip_code = USZipCodeField

class Person(models.Model):
    ETHNICITY_CHOICES = [
        ('american indian or alaskan native', 'American Indian or Alaskan Native'),
        ('asian', 'Asian'),
        ('black or african-american', 'Black or African-American'),
        ('hispanic or latino', 'Hispanic or Latino'),
        ('native hawaiian or other pacific islander', 'Native Hawaiian or Pacific Islander'),
        ('white', 'White'),
        ('bi-racial', 'Biracial'),
        ('multiracial', 'Multiracial'),
        ('other', 'Other'),
        ('decline to self identify', 'Decline to Self Identify')
    ]
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    ethnicity = models.ChoiceField(max_length=30, choices=ETHNICITY_CHOICES)
    sex = models.ChoiceField(max_length=6, choices=SEX_CHOICES)
    address1 = models.ForeignKey(Address, on_delete=models.CASCADE)
    address2 = models.CharField(max)
    five_plus_at_address = models.BooleanField(default=False)
    years_of_service = models.IntegerField(max_length=2)




