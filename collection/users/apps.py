from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'collection.users'
    label = 'users'

    def ready(self):
        """Override this to put in:
            Lives system checks
            Lives signal registration
        """
        pass
