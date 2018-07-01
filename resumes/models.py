from django.db import models

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=250)
    skills = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    addActivity = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
