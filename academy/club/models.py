from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=255)
    scores = models.IntegerField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)


    def __str__(self):
        return self.name