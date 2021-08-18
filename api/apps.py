from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from . import background_tasks

        if os.environ.get('RUN_MAIN', None) == 'true':
            background_tasks.start_scheduler()
