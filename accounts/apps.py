from django.apps import AppConfig
# from django.utils.translation import ugettext_lazy as _

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    def ready(self):
        from . import signals



    