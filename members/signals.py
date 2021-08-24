from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from myPlog.models import Post
from .models import Profile

# @receiver(post_save,sender=User)
def create_or_save_user_profile(sender,instance,created,**kwargs):
    
    if created:
        group=Group.objects.get(name=instance)
        instance.groups.add(group)
        Profile.objects.create(
			user=instance,
			name=instance.username,
			)
        print('Profile created!')

    
post_save.connect(create_or_save_user_profile, sender=User)
