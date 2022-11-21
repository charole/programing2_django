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
    age = models.IntegerField(default=0)
    point = models.IntegerField(null=True)


class Example(models.Model):
    EXAM_TYPES = (
        ('Multiple', 'Multiple'),
        ('Simple', 'Simple')
    )

    id = models.AutoField(db_column='id', primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    exam_question = models.TextField(default='', null=True, blank=True)
    exam_type = models.CharField(choices=EXAM_TYPES, max_length=10)
    answer = models.TextField(default='')
    example = models.TextField(default='', null=True, blank=True)
    hint = models.TextField(default='', null=True, blank=True)
    point = models.IntegerField(default=0, null=True)
    level = models.IntegerField(default=0, null=True, blank=True)
