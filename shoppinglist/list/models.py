from django.db import models


class Product(models.Model):
    UNITS = (
        ('kg', 'kg'),
        ('g', 'g'),
        ('lbs', 'lbs'),
        ('liters', 'liters'),
        ('ml', 'ml'),
    )
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True, choices=UNITS)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Notes(models.Model):
    notes = models.TextField(max_length=3000, null=True, blank=True)
