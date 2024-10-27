from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.contrib.postgres.fields import ArrayField
# from enum import Enum

# Create your models here.

'''
class locationConstants(Enum):
    WILEY = 'Wiley'
    EARHART = 'Earhart'
    WINDSOR = 'Windsor'
    HILLENBRAND = 'Hillenbrand'
    FORD = 'Ford'
    ANY = 'Any'

class timeConstants(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    LATELUNCH = 'Late Lunch'
    BRUNCH = 'Brunch'
    ANY = 'Any'
'''

class Menu(models.Model):

    name = models.CharField(max_length=200)
    # servingSize = models.CharField(max_length=30, default = "1 serving")
    # calories = models.IntegerField(default = 0)
    # ingredients = models.CharField(max_length=2500)
    vegetarian = models.BooleanField(default = False)
    vegan = models.BooleanField(default = False)
    glutenFree = models.BooleanField(default = False)
    dairy = models.BooleanField(default = False)
    peanuts = models.BooleanField(default = False)
    soybean = models.BooleanField(default = False)
    wheat = models.BooleanField(default = False)
    eggs = models.BooleanField(default = False)
    coconut = models.BooleanField(default = False)
    fish = models.BooleanField(default = False)
    shellfish = models.BooleanField(default = False)
    sesame = models.BooleanField(default = False)
    # totalFat = models.CharField(max_length=10, default = '0g')
    # saturatedFat = models.CharField(max_length=10, default = '0g')
    # cholesterol = models.CharField(max_length=10, default = '0mg')
    # sodium = models.CharField(max_length=10, default = '0mg')
    # totalCarbohydrate = models.CharField(max_length=10, default = '0g')
    # sugar = models.CharField(max_length=10, default = '0g')
    # addSugar = models.CharField(max_length=10, default = '0g')
    # dietaryFiber = models.CharField(max_length=10, default = '0g')
    # protein = models.CharField(max_length=10, default = '0g')
    # locations = ArrayField(models.CharField(max_length=25, default = None), default = None)
    '''
    locations = ArrayField(models.CharField(max_length=25,
        choices=[(location.value, location.name) for location in locationConstants],
        default=locationConstants.ANY.value), default = None)
    times = ArrayField(models.CharField(max_length=20,
        choices=[(time.value, time.name) for time in timeConstants],
        default=timeConstants.ANY.value), default = None)
    '''


class UserManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        if not username:
            raise ValueError("Username required")
        if not password:
            raise ValueError("Password required")
        user=self.model(
            username=self.username,
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    vegetarian = models.BooleanField(default = False)
    vegan = models.BooleanField(default = False)
    glutenFree = models.BooleanField(default = False)
    dairy = models.BooleanField(default = False)
    peanuts = models.BooleanField(default = False)
    soybean = models.BooleanField(default = False)
    wheat = models.BooleanField(default = False)
    eggs = models.BooleanField(default = False)
    coconut = models.BooleanField(default = False)
    fish = models.BooleanField(default = False)
    shellfish = models.BooleanField(default = False)
    sesame = models.BooleanField(default = False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['password']
    objects=UserManager()