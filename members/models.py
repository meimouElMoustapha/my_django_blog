from django.db import models
from django.contrib.auth.models import User

# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from django.contrib import auth
# Create your models here.

class Profile(models.Model):
        user=models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
        
        bio=models.CharField(max_length=200)
        location=models.CharField(max_length=200)
        language=models.CharField(max_length=200)
        image_field=models.ImageField(upload_to="media/",default="media/image3.jpg")
        
        def __str__(self):
            return F'{self.user.username} Profile'
 
        
# @receiver(post_save,sender=User)
# def create_or_save_user_profile(sender,created,instance,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
    
#     instance.profile.save()

    
