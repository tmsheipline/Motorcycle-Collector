from django.db import models
from django.urls import reverse
from datetime import date

TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

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

    def wash_for_today(self):
        return self.washing_set.filter(date=date.today()).count() >= len(TIME)


class Washing(models.Model):
    date = models.DateField('Washing/Detail Date')
    time = models.CharField(max_length=1,
                            choices=TIME,
                            default=TIME[0][0])


    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"


    class Meta:
        ordering = ['-date']
