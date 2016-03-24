from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    
    def __unicode__(self):
        return self.title