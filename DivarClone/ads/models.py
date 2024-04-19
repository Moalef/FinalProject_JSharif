from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                               null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name
