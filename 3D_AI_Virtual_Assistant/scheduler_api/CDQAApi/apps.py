from django.apps import AppConfig
from . import driver_module

class CdqaapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CDQAApi'

    def ready(self):
        # Code to run when the server starts
        driver_module.initialize_driver()
