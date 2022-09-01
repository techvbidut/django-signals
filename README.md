# django_signals

1. Accounts is an app created in this project.
2. Inside accounts app, signals.py is created and all the signal receivers are defined.
3. Inside apps.py, we have imported signals.py inside ready function.
4. Not created various APIs to complicate the topic. So, refer the steps below for testing signals.

A. For testing pre_save and post_save signals.
  1. Create a super user and add Resource object from admin panel.
  2. On the terminal you should see the pre_save and post_save print message.
  
B. For testing pre_delete and post_delete signals.
  1. Create a super user and add Resource object from admin panel.
  2. In the terminal type `python manage.py shell`
  3. Inside the shell run: `from accounts.models import Resource` and `Resource.objects.all().delete()`
  3. On the terminal you should see the pre_delete and post_delete print message.
