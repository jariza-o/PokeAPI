from rest_framework.serializers import ModelSerializer
from custom_auth.models import Custom_User

class MessagesSerializer(ModelSerializer):
    """
    Serializers:
        Transform the model information to JSON format

    Args:
        ModelSerializer:
            Class from Django Rest Framework used for create serializers.
    """
    class Meta:
        model = Custom_User
        fields = ['email', 'password']