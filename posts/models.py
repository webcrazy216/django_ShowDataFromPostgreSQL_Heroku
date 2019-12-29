from django.db import models

# Create your models here.
class Personaldatas(models.Model):
    imgurl = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.FloatField()
    level = models.IntegerField()
    goals = models.IntegerField()
    achived = models.IntegerField()
    gender = models.BooleanField(default=False)

