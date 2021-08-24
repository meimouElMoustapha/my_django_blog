from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True,blank=True )
    updated=models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
        

class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    from_signal=models.BooleanField(default=False)
    bio=models.CharField(max_length=200)
    image=models.ImageField(upload_to="uploads/")
    age=models.IntegerField()
    
    
    def __str__(self):
        return self.bio
    

class Post(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    field =models.CharField(max_length=200)
    content=models.TextField()
    comment=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    Image=models.ImageField(upload_to="uploads/",null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    
        

    
