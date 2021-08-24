from django.db.models.signals import post_save #,pre_save
from .models import Task
from django.contrib.auth.models import User
from django.dispatch import receiver



@receiver(post_save,sender=User)
def post_save_create_user(sender,instance,created,**kwargs):
    print ('sender',sender)
    print ('instance',instance)
    print ('created',created)
    if created:
        Task.objects.create(user=instance)

# def rl_pre_save_receiver(sender,instance,*args, **kwargs):
#     print("awsome data saved ")
#     print(instance.created)
    
# def rl_post_save_receiver(sender,instance,*args, **kwargs):
#     print("awsome data saved ")
#     print(instance.created)

# pre_save.connect(rl_pre_save_receiver,sender=Task)
# pre_save.connect(rl_post_save_receiver,sender=Task)