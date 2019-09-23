from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from recipe_app.views.user import UserViewSet
from recipe_app.views.recipe import RecipeViewSet, IngredientViewSet, StepViewSet
from django.urls import path


app_name = 'recipe_app'
router = DefaultRouter()
router.register('ingredients', IngredientViewSet)
router.register('steps', StepViewSet)
urlpatterns = [
    path('create_user/',
         UserViewSet.as_view({'post': 'create'}), name='create_user'),
    path('', include(router.urls)),
    path('recipe/', RecipeViewSet.as_view({
        'post': 'create',
        'get': 'list'
        }), name='create_recipe'),
    path('recipe/user/<uuid:userId>/', RecipeViewSet.as_view({'get': 'retrieve'}), name='user_recipe'),
    path('recipe/<uuid:pk>/', RecipeViewSet.as_view({
         'get': 'get_recipe',
         'delete': 'destroy' 
         }), name='get_recipe')
]
