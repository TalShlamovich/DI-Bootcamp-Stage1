from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)


class Animal(models.Model):
    name = models.CharField(max_length=50, null=True) 
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, null = True, on_delete = models.SET_NULL, related_name='posts')

    def __str__(self) -> str:
        return self.id + ' ' + self.legs + ' ' + self.height + ' ' + self.weight + ' ' + self.speed + ' ' + self.family