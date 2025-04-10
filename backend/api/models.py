from django.db import models
from django.contrib.auth.models import Userfrom

# Create your models here.
class Subject(models.Model):    
    title = models.CharField(max_length=200)    
    slug = models.SlugField(max_length=200, unique=True)    

    class Meta:        
        ordering = ['title']   

    def __str__(self):        
        return self.title


