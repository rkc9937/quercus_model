from django.db import models
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

class Professors(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    classes = ListCharField(
        base_field = CharField(max_length=8),
        size = 5 #Max classes someone can take is 5. Imported mySQL to avoid tuple implmentation
    )

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    professors = models.ForeignKey(Professors, on_delete=models.CASCADE) # Many students can have many professors.
    classes = ListCharField(
        base_field = CharField(max_length=8),
        size = 5 #Max classes someone can take is 5. Imported mySQL to avoid tuple implmentation
    )

