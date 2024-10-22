from rest_framework.routers import DefaultRouter
from custom_auth.api.views import login_view

"""
Use:
    Configure the router for the API
"""

router_chat = DefaultRouter()

"""
Use:
    Register a View Sets whit the router

Parameters:
    prefix='chat':
        Specific the URL for this View Sets
    basename='chat':
        Specific the base name for the URLs generated.
    viewset=MessagesApiViewSet:
        Specific the View Sets to be register.
"""
router_chat.register(prefix='auth', basename='auth', viewset=login_view)