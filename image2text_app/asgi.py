"""
ASGI config for image2text_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "image2text_app.settings")

# Get the default Django ASGI application
django_asgi_app = get_asgi_application()

# Example of adding a middleware - adjust the import path as necessary
# This is a placeholder for actual middleware you might want to use
class CustomMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # Example middleware logic: modify scope or handle requests/responses
        # You can modify the incoming scope or intercept requests/responses
        # For example, adding a header or logging request data
        print("Custom Middleware: Handling request")
        await self.app(scope, receive, send)  # Continue to the next application

# Wrap the Django ASGI application with the custom middleware
application = CustomMiddleware(django_asgi_app)

