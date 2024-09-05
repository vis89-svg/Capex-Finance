from django.db import models




class Movie(models.Model):
    name=models.CharField(max_length=100)
    genere=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)

def _str_(self):
    return self.name

