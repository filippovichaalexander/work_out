from django.db import models

class TrainingPlans(models.Model):
    name = models.CharField(max_length=200, null=False)
    level = models.CharField(max_length=200, null=False)
    number_of_sets = models.FloatField()
