from django.apps import AppConfig


class GamesConfig(AppConfig):
    name = 'collection.games'
    label = 'games'

    def ready(self):
        """Override this to put in:
            Lives system checks
            Lives signal registration
        """
        pass
