# Django Signals

## What are Signals in Django?
1. Signals simply means a gesture, action, or sound that is used to convey information or instructions
2. In our context signals are the connection between an event and action.
3. Let us understand with an example, Event is saving a comment and the action is filtering out the abusive words in the comment. This was just an usecase of signals. We will understand more about it later.
3. Now lets go through the definintion of Django signals. Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework. In a nutshell, <b>signals allow certain senders to notify a set of receivers that some action has taken place.</b>
4. Basically, signals are used to perform any action on modification of a model instance.

## Terms to know
1. Receiver: The function or action that will be executed when an action takes place.
2. Sender: The Model name which will send the signal.

## Types of signals
1. <b>pre_save/post_save:</b> Works before/after the method save().
2. <b>pre_delete/post_delete:</b> Works before/after the method delete().
3. <b>pre_init/post_init:</b> Works before/after instantiating a model (__init__() method).


### Let us understand the project structure for this project
1. Accounts is an app created in this project.
2. Inside accounts app, signals.py is created and all the signal receivers are defined.
3. Inside apps.py, we have imported signals.py inside ready function.
4. I have not created various APIs to complicate the topic. So, refer the steps below for testing this project.

### Lets now see how the code will look like

Inside the accounts app we will create a new file `signals.py` and write the code below in it:
```
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Resource

# pre_save method signal
@receiver(pre_save, sender=Resource)
def pre_save_res(sender, instance, **kwargs):
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
```

Also, the `apps.py` will look something like this:
```
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    def ready(self):
        from . import signals
```

### Steps to follow if you have cloned this repository
1. Run the command ``

### How to test?
<b>A. For testing pre_save and post_save signals.</b>
  1. Create a super user and add Resource object from admin panel.
  2. On the terminal you should see the pre_save and post_save print message.
  
<b>B. For testing pre_delete and post_delete signals.</b>
  1. Create a super user and add Resource object from admin panel.
  2. In the terminal type `python manage.py shell`
  3. Inside the shell run: `from accounts.models import Resource` and `Resource.objects.all().delete()`
  3. On the terminal you should see the pre_delete and post_delete print message.
