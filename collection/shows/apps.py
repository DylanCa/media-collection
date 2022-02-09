from django.apps import AppConfig


class ShowsConfig(AppConfig):
    name = 'collection.shows'
    label = 'shows'

    def ready(self):
        """Override this to put in:
            Lives system checks
            Lives signal registration
        """
        pass
