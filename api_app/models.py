from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.name
