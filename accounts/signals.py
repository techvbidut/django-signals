from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Resource

# pre_save method signal
@receiver(pre_save, sender=Resource)
def pre_save_res(sender, instance, **kwargs):
    # if not instance.description:
    #     instance.description = 'This is Default Description'
    print(" You are about to Save...") 

# post_save method
@receiver(post_save, sender=Resource) 
def post_save_res(sender, instance, created, **kwargs):
    print("Save method is called") 

@receiver(pre_delete, sender=Resource)
def pre_delete_res(sender, **kwargs):
    print("You are about to delete something!")

@receiver(post_delete, sender=Resource)
def delete_res(sender, **kwargs):
    print("You have just deleted a resource!!!")