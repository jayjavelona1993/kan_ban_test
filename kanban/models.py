from django.db import models

# Create your models here.
class Stage(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    sequence = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    stage = models.ForeignKey(Stage, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name
