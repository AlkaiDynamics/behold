from django.apps import AppConfig

class Image2TextAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image2text_app'
    verbose_name = 'Image to Text Application'

    def ready(self):
        # Initialization code that runs when the app is ready.
        pass
