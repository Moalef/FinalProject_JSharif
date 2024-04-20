from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                               null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status = Ad.Status.PUBLISHED)



class Ad (models.Model):
    class Status(models.TextChoices):
        DRAFT = ('DF' , 'Draft')
        PUBLISHED = ('PB' , 'Published')

    title = models.CharField(max_length = 250)
    owner = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'ads')
    description = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 2 , choices = Status.choices , default = Status.DRAFT)
    

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish' ]
        indexes = [models.Index(fields= ['-publish'])]

    
    def __str__(self):
        return self.title
    