from django.apps import AppConfig
import sys

class ShowApiDataConfig(AppConfig):
    name = 'show_api_data'
    def ready(self):

        if 'runserver' in sys.argv:
            from sceduler import sceduler
            sceduler.start()
