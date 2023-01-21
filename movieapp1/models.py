from django.db import models

# Create your models here.
class movies(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField()
    year_released=models.IntegerField()
    desc=models.IntegerField()
    image=models.CharField(max_length=30)