from django.db import models
from django.contrib.auth.models import AbstractUser


# Shorthand

class shows_name:
    def __str__(self):
        return self.name


# Models
        """Stage -> Grade -> Class -> Student"""

# Primary, Preparatory, and Secondary
class Stage(models.Model, shows_name):
    name = models.CharField(max_length=20)


# 1st secondary, etc...
class Grade(models.Model, shows_name):
    name = models.CharField(max_length=20)
    stage = models.ForeignKey('Stage', models.CASCADE)


# 1st secondary - 5th class
class Class(models.Model, shows_name):
    name = models.CharField(max_length=20)
    grade = models.ForeignKey('Grade', models.CASCADE)
    class_price = models.SmallIntegerField() # the price of each class
    additional_price = models.SmallIntegerField() # if the teacher required additional money


# 1st secondary - 5th class - (name: Mahmoud Abdelatte Shalaby)
class Student(models.Model, shows_name):
    name = models.CharField(max_length=40)
    _class = models.ForeignKey('Class', models.CASCADE)
    got_classes = models.SmallIntegerField() # classes student has gotten
    left_classes = models.SmallIntegerField() # classes student has never gotten
    paid_money = models.SmallIntegerField()
    required_money = models.SmallIntegerField() # equals to (got_classes * _class.class_price)
