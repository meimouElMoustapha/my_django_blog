from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import User
from members.models import Profile


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    profile=models.ForeignKey(Profile,null=True, on_delete= models.SET_NULL)
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    field=models.CharField(max_length=200)
    content=models.TextField()
    comment = models.CharField(max_length=200)
    Image=models.ImageField(upload_to="media/")
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("home")
    
# @receiver(post_save,sender=User)
# def create_or_save_user_profile(sender,created,instance,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
    
#     instance.profile.save()