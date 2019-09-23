from django.shortcuts import get_object_or_404, render
from recipe_app.models.app import Ingredient, Recipe, Step
from recipe_app.serializers import (IngredientSerializer, ListRecipeSerializer,
                                    RecipeSerializer, StepSerializer)
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from recipe_app.helpers.check_resource import resource_exists, check_resource, save_serializer, get_response

def _params_to_ints(qs):
    """Convert a (string) list of string ids to a list of integers"""
    return [int(str_id) for str_id in qs.split(',')]


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):

    def get_queryset(self):
        """Return objects for current auth'ed user only"""
        return self.queryset.filter().order_by('id')

    def perform_create(self, serializer):
        """Create new object"""
        serializer.save()


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage Ingredients in database"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class StepViewSet(BaseRecipeAttrViewSet):
    """Manage Step in database"""
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class RecipeViewSet(ViewSet):
    """Users viewset."""

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        """Return objects for current auth'ed user only"""
        return self.queryset.filter().order_by('id')

    def create(self, request):
        """
        Create a Recipe
        If successful, response payload with:
            - status: 200
            - data
        If unsuccessful, a response payload with:
            - status: 400
            - error: Bad Request
            - message
            Status Code: 400
        Request
        -------
        method: post
        url: /api/v1/recipe/
        """
        serializer = RecipeSerializer(
            data=request.data)
        if serializer.is_valid():
            data = save_serializer(serializer)
            return Response(data, status=status.HTTP_201_CREATED)
        data = {
            'status': 'error'
        }

        data.update({'data': serializer.errors})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response(data, status=status_code)


    def list(self, request):
        """
        Get all recipe.
        Returns
        -------
        If successful:
            A response payload with:
            - status code: 200
            - data
            The data is a list of recipe objects.
            The dictionaries resemble the data in a single recipe response.
        If unsuccessful:
            A response payload with:
            - status code: 404
            - error: recipe_not_found
            - message.
        Request
        -------
        method: get
        url: /api/v1/recipe/
        """
        recipes = self.queryset
        query = request.query_params.get('q')
        if query:
            recipes = self.queryset.filter(Q(name__icontains=query))
        serializer = ListRecipeSerializer(recipes, many=True)
        return Response(serializer.data)


    def retrieve(self, request, userId=None):
        """
        Get recipe with User.
        Returns
        -------
        If successful:
            A response payload with:
            - status code: 200
            - data
            The data is a list of recipe objects.
            The dictionaries resemble the data in a single recipe response.
        If unsuccessful:
            A response payload with:
            - status code: 404
            - error: recipe_not_found
            - message.
        Request
        -------
        method: get
        url: /api/v1/recipe/user/<userId>
        """
        
        return Response(*check_resource(Recipe, ListRecipeSerializer, 'user', userId, request, "Recipe"))


    def get_recipe(self, request, pk=None):
        """
        Get a Recipe.
        If successful, response payload with:
            - status code: 200
            - data
        The response payload has keys:
            - id
            - name
            - user
            - ingredient
            - step
            - created_at
        If unsuccessful, a response payload with:
            - status code: 404
            - error: activity_not_found
            - message: Ensure the ID passed is of an existing Recipe.
        Request
        -------
        method: get
        url: /api/v1/recipe/<pk>
        """

        return Response(*check_resource(Recipe, ListRecipeSerializer, 'pk', pk, request, "Recipe"))
        

    def destroy(self, request, pk=None):
        """
        Delete an Recipe.
        If unsuccessful, a response payload with:
            - status code: 404
            - error: recipe_not_found
            - message: Ensure the ID passed is of an existing recipe.
        If successful, a response payload with:
            - status code: 200
            - messsage: recipe deleted successful
        Request
        -------
        method: delete
        url: /api/v1/recipe/<pk>
        """
        recipe = resource_exists(Recipe, 'pk', pk)
        if not recipe:
            response_attr = {'format_str': 'Recipe', 'error_key': 'not_found'}
            data = get_response(**response_attr)
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        data = {
            'status': 'success',
            'message': 'recipe deleted successfully'
            }
        return Response(data, status=status.HTTP_200_OK)
