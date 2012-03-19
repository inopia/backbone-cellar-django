from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    grapes = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField(upload_to="wines/")

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.save()

