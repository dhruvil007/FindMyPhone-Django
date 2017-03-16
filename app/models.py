from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_id = models.CharField(blank=False, max_length=250)
    model = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return_string = self.user.username + ' - ' + self.model
        return return_string