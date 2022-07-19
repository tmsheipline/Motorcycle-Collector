from django.db import models
from django.urls import reverse

# Create your models here.
class Motorcycle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.make
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'motorcycle_id': self.id})
