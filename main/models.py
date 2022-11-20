from pickle import TRUE
from django.db import models

# Create your models here.


class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.postname


class Account(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    point = models.IntegerField(null=True)

class Example(models.Model):
    index = models.IntegerField(db_column='idx', primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    exam_question = models.TextField()
    answer = models.TextField()
    example = models.TextField()
    point = models.IntegerField()

    
