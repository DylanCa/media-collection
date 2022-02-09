from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = 'collection.movies'
    label = 'movies'

    def ready(self):
        """Override this to put in:
            Lives system checks
            Lives signal registration
        """
        pass
