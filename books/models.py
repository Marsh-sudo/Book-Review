
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200,blank=True)
    author = models.CharField(max_length=200,blank=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    logo = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=200,blank=True)
    pages = models.IntegerField(blank=True,default=1)
    price = models.IntegerField(blank=True,default=1)



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=200,blank=True)
    name = models.CharField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='images/')


class Review(models.Model):
    title = models.CharField(max_length=300,blank=True)
    post = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    book = models.ForeignKey(Books,on_delete=models.CASCADE,related_name='books',blank=True,null=True)
