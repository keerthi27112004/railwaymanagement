from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return self.name
