from distutils.command.upload import upload
from email.mime import image
from enum import auto
from pyexpat import model
from tabnanny import verbose
# from turtle import title
from unicodedata import category, name
from venv import create

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

# Post 
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    contents = models.TextField()
    published = models.BooleanField(default=False)
    tags = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title
        
