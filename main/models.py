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
    clear_example_count = models.IntegerField(default=0, null=True, blank=True)


class Example(models.Model):
    EXAM_TYPES = (
        ('Multiple', 'Multiple'),
        ('Simple', 'Simple')
    )

    LEVEL = (
        ('하', '하'),
        ('중', '중'),
        ('상', '상')
    )

    id = models.AutoField(db_column='id', primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    exam_question = models.TextField(default='', null=True, blank=True)
    exam_type = models.CharField(
        choices=EXAM_TYPES, default='Simple', max_length=10)
    example = models.TextField(default='', null=True, blank=True)
    answer = models.TextField(default='')
    hint = models.TextField(default='', null=True, blank=True)
    point = models.IntegerField(default=0, null=True, blank=True)
    level = models.CharField(choices=LEVEL, default='하', max_length=1)
