from django.db import models


class Fee(models.Model):
    name = models.CharField('Name', max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.name
