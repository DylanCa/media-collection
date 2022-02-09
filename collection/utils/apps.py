from django.apps import AppConfig

class UtilsConfig(AppConfig):
    name = 'collection.utils'
    label = 'utils'

    def ready(self):
        """Override this to put in:
            Lives system checks
            Lives signal registration
        """
        pass
