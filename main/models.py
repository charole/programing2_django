from django.db import models

# Create your models here.


class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.postname


class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()


class Example(models.Model):
    exam_index = models.IntegerField()
    title = models.CharField(max_length=10)
