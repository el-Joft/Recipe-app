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


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'ingd_text')
        read_only_fields = ('id',)
        

class StepSerializer(serializers.ModelSerializer):
    """Serializer for step objects"""

    class Meta:
        model = Step
        fields = ('id', 'text_step')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """
    Recipe Model Serializer.
    """
    
    ingredient = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    ingredients = IngredientSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    
    step = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Step.objects.all()
    )
    steps = IngredientSerializer(read_only=True)
    class Meta:
        """Access fields and create returned object."""
        model = Recipe
        fields = ('id', 'name', 'user', 'ingredients', 'step',
                'steps', 'ingredient','created_at', 'updated_at',)


class ListRecipeSerializer(RecipeSerializer):

    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)
    user = UsersSerializer(read_only=True)
    class Meta:
        """Access fields and create returned object."""
        model = Recipe
        fields = ('id', 'name', 'user',
                'steps', 'ingredients','created_at', 'updated_at',)
