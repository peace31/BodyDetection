from rest_framework import serializers
from api.models import UserInput


class UserInputSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = UserInput
        fields = ('image', 'picture', 'gender', 'angle', 'user_id',)
