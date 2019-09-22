import re

from recipe_app.models.app import Ingredient, Recipe, Step, User
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    """
    Users Model Serializer.
    """
    class Meta:
        """Access fields and create returned object."""
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'username', 'password',
                  'created_at', 'updated_at',)
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, validated_data):
        errors = []
        for (key, value) in validated_data.items():
            if key == 'password':
                if re.match('^([a-z]*|[A-Z]*|[0-9]*|.{0,7})$', value):
                    errors.append(
                        "Password must contain a Number,"
                        + " a letter and 8 charcters long"
                    )
        if len(errors) > 0:
            raise serializers.ValidationError(errors)

        return validated_data
